#!/usr/bin/env bash
# Preview the site locally at http://localhost:4000/OUE3e/
#
# Usage (from anywhere):  scripts/preview.sh
#
# Uses Homebrew's Ruby if it is installed, and a throwaway Gemfile kept in
# ~/.cache/oue3e-preview so the project's own Gemfile and Gemfile.lock stay untouched.
# (Ruby 4 no longer bundles gems that Jekyll 4.3 needs; the project Gemfile targets Ruby 3.3.)
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CACHE="$HOME/.cache/oue3e-preview"

# Prefer Homebrew Ruby over the old system Ruby
for dir in /opt/homebrew/opt/ruby/bin /usr/local/opt/ruby/bin; do
  [ -x "$dir/ruby" ] && export PATH="$dir:$PATH" && break
done
export PATH="$(gem env gemdir)/bin:$PATH"
echo "Using $(ruby -v)"

mkdir -p "$CACHE"
cat > "$CACHE/Gemfile" <<'EOF'
source "https://rubygems.org"
gem "jekyll", "~> 4.4.1"
gem "just-the-docs", "0.10.1"
gem "logger"
gem "csv"
gem "base64"
gem "bigdecimal"
gem "webrick"
EOF

export BUNDLE_GEMFILE="$CACHE/Gemfile"
export BUNDLE_PATH="$CACHE/vendor"
bundle install --quiet

cd "$REPO"
# --livereload refreshes the browser when you save a file; --baseurl matches GitHub Pages
exec bundle exec jekyll serve --source . --destination "$CACHE/_site" \
  --baseurl /OUE3e --livereload
