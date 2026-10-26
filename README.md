# Observing the User Experience: companion site

Source for the companion website of *Observing the User Experience*, third edition, by Elizabeth Goodman and Mike Kuniavsky. Live at <https://mikekuniavsky.github.io/OUE3e/>.

The site is built with [Jekyll](https://jekyllrb.com) and the [Just the Docs](https://just-the-docs.com) theme, and deployed to GitHub Pages by `.github/workflows/pages.yml` on every push to `main`.

It does **not** contain the book's text. It has an overview of each chapter, a searchable bibliography built from the book's Zotero library, and a page of the links and tools mentioned in the chapters.

## Layout

| Path | What it is |
|---|---|
| `index.md`, `about.md`, `resources.md`, `bibliography.md` | Top-level pages |
| `chapters/*.md` | One thin page per chapter (front matter only) |
| `_layouts/chapter.html` | Template that fills each chapter page from the data files |
| `_data/chapters.yml` | **Chapter content**: titles, summaries, sections, key terms, links |
| `_data/zotero.json` | Bibliography, generated from Zotero (do not edit by hand) |
| `_data/authors.yml` | Author names and LinkedIn URLs |
| `_data/book.yml` | Where to buy the book (Elsevier, Amazon US) |
| `_includes/author.html`, `_includes/authors.html` | Print an author's name (or both) with a LinkedIn icon |
| `_includes/footer_custom.html` | The footer on every page |
| `_includes/components/aux_nav.html` | **Overrides the theme's header links** (see below) |
| `scripts/fetch_zotero.py` | Downloads the Zotero library into `_data/zotero.json` |
| `scripts/preview.sh` | Builds and serves the site locally |
| `_sass/custom/custom.scss` | Site styles |

## Common tasks

**Edit a chapter's description, title or links.** Edit its entry in `_data/chapters.yml`. Titles live there, so one edit updates the navigation, the chapter page, the home page and the chapter list.

**Add or remove a chapter.** Add an entry to `_data/chapters.yml` and a matching `chapters/<slug>.md` page (copy any existing one and change `title`, `chapter`, `nav_order` and `permalink`).

**Change the "Buy the book" links or an author's LinkedIn.** Edit `_data/book.yml` or `_data/authors.yml`. The home page, About page and footer read from them. Leave a `linkedin:` value empty to show the name without an icon.

**Change the header links.** The links in the top right come from two places:

- **"Buy the book"** is written directly in `_includes/components/aux_nav.html`. That file overrides the theme's own `aux_nav.html` (Jekyll uses the copy in the site before the copy in the theme gem). We did this because the theme's version prints each link exactly as written in `_config.yml`, so it can't link to a page on this site (it skips `relative_url`, which matters because the site lives under `/OUE3e/`), and it opens every link in a new tab. Our copy sends "Buy the book" to `/#get-the-book` in the same tab, then loops over `aux_links` in `_config.yml` for the rest. Its look is the `.buy-button` rule in `_sass/custom/custom.scss`.
- **"Zotero library" and "GitHub"** come from `aux_links` in `_config.yml`. To add or remove one of those, edit that list. Don't add "Buy the book" there; it's already in the override.

If you upgrade `just-the-docs` (the version is pinned in the `Gemfile`), compare our `aux_nav.html` with the new theme's copy (`bundle info just-the-docs` shows where the gem lives, then look in `_includes/components/aux_nav.html`) and carry over any changes. To go back to the theme's version, delete our file and move "Buy the book" into `aux_links` with the full URL.

**Refresh the bibliography.** The Zotero group library (`https://www.zotero.org/groups/5691168/oue/library`) is public, so no key is needed:

```bash
python3 scripts/fetch_zotero.py
git add _data/zotero.json
git commit -m "Refresh bibliography from Zotero"
```

The script reads the library's collections: a collection named "Chapter N ..." (or a sub-collection of one) assigns its items to chapter N, which is what drives each chapter's "Further reading" list. Items that are in no chapter collection appear only in the full bibliography.

**Preview locally.** From the repo, run:

```bash
scripts/preview.sh
```

Then open <http://localhost:4000/OUE3e/>. The page refreshes when you save a file. The script uses Homebrew's Ruby and a throwaway Gemfile in `~/.cache/oue3e-preview`, because Ruby 4 no longer bundles gems that Jekyll 4.3 needs (`logger`, `csv`, `base64`, `bigdecimal`, `webrick`), and we'd rather not change the project's Gemfile (GitHub's build uses Ruby 3.3). If you're on Ruby 3.x, `bundle install` and `bundle exec jekyll serve` work too.

## Open items

These came up while building the first version and need an author decision:

- **Chapter 11 title.** The manuscript title is "Diary Studies"; other chapters and Zotero call it "Learning Over Time". The site uses "Diary Studies".
- **Chapter 3 has no readings.** Zotero's "Chapter 3" collection is empty, so that chapter has no further reading.
- **Chapters 2 and 7 titles** also vary across the manuscript ("Program Roadmapping" vs. "Research Program Roadmapping", "Learning from Observation" vs. "Learning From Observation"). The site uses the first form of each.
- **Uncollected items.** About 27 Zotero items are not in any chapter collection; they only appear in the full bibliography.
- **Links** on the chapter pages are the ones printed in the manuscript. A link checker run before launch would be sensible.
- **Chapter 18 tool link.** The data-management workshop tool is credited to "Consent Kit" in the manuscript and to "Participant Kit" in the proofs, so no link is included yet.
