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
| `scripts/fetch_zotero.py` | Downloads the Zotero library into `_data/zotero.json` |
| `_sass/custom/custom.scss` | Site styles |

## Common tasks

**Edit a chapter's description, title or links.** Edit its entry in `_data/chapters.yml`. Titles live there, so one edit updates the navigation, the chapter page, the home page and the chapter list.

**Add or remove a chapter.** Add an entry to `_data/chapters.yml` and a matching `chapters/<slug>.md` page (copy any existing one and change `title`, `chapter`, `nav_order` and `permalink`).

**Refresh the bibliography.** The Zotero group library (`https://www.zotero.org/groups/5691168/oue/library`) is public, so no key is needed:

```bash
python3 scripts/fetch_zotero.py
git add _data/zotero.json
git commit -m "Refresh bibliography from Zotero"
```

The script reads the library's collections: a collection named "Chapter N ..." (or a sub-collection of one) assigns its items to chapter N, which is what drives each chapter's "Further reading" list. Items that are in no chapter collection appear only in the full bibliography.

**Preview locally.** Install Ruby 3.x, then:

```bash
bundle install
bundle exec jekyll serve
```

Then open <http://localhost:4000/OUE3e/>.

With Ruby 4.x, Jekyll 4.3 also needs gems that Ruby no longer bundles (`logger`, `csv`, `base64`, `bigdecimal`, `webrick`). Rather than changing the project's Gemfile (GitHub's build uses Ruby 3.3), use a throwaway Gemfile outside the repo that lists them next to `jekyll` and `just-the-docs`, and run `BUNDLE_GEMFILE=/path/to/that/Gemfile bundle exec jekyll serve --source .`.

## Open items

These came up while building the first version and need an author decision:

- **Chapter 11 title.** The manuscript title is "Diary Studies"; other chapters and Zotero call it "Learning Over Time". The site uses "Diary Studies".
- **Chapter 3 has no readings.** Zotero's "Chapter 3" collection is empty, so that chapter has no further reading.
- **Chapters 2 and 7 titles** also vary across the manuscript ("Program Roadmapping" vs. "Research Program Roadmapping", "Learning from Observation" vs. "Learning From Observation"). The site uses the first form of each.
- **Uncollected items.** About 27 Zotero items are not in any chapter collection; they only appear in the full bibliography.
- **Links** on the chapter pages are the ones printed in the manuscript. A link checker run before launch would be sensible.
- **Chapter 18 tool link.** The data-management workshop tool is credited to "Consent Kit" in the manuscript and to "Participant Kit" in the proofs, so no link is included yet.
