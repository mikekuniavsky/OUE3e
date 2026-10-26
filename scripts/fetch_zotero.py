#!/usr/bin/env python3
"""Fetch the public OUE Zotero group library and write _data/zotero.json.

Usage (from the repo root):
    python3 scripts/fetch_zotero.py

The Zotero group library is public, so no API key is needed. The script uses only
the Python standard library. It writes one record per top-level library item with:

  key          Zotero item key
  title        item title
  year         publication year (string, may be empty)
  sort         lowercase key used to alphabetize (first creator, then title)
  type         Zotero item type
  url          item URL if it has one (otherwise the DOI link, otherwise "")
  zotero       link to the item in the Zotero web library
  bib          APA-style citation as an HTML snippet (from the Zotero API)
  chapters     sorted list of chapter numbers whose collection contains the item
               (0 = Preface). Sub-collections count toward their parent chapter.

Re-run the script whenever the library changes, then commit _data/zotero.json.
"""
import html
import json
import re
import sys
import time
import urllib.request

GROUP_ID = 5691168
API = f"https://api.zotero.org/groups/{GROUP_ID}"
STYLE = "apa"
OUT = "_data/zotero.json"


def get(url):
    req = urllib.request.Request(url, headers={"Zotero-API-Version": "3"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp), resp.headers
        except Exception as exc:  # network hiccup or rate limit: back off and retry
            if attempt == 3:
                raise
            print(f"  retry after error: {exc}", file=sys.stderr)
            time.sleep(2 * (attempt + 1))


def fetch_all(path, params):
    items, start = [], 0
    while True:
        url = f"{API}/{path}?{params}&limit=100&start={start}"
        batch, headers = get(url)
        items.extend(batch)
        total = int(headers.get("Total-Results", len(items)))
        start += 100
        if start >= total:
            return items
        time.sleep(0.5)


def chapter_of_collection(collections):
    """Map every collection key to a chapter number (sub-collections inherit)."""
    by_key = {c["key"]: c for c in collections}

    def resolve(key):
        seen = set()
        while key and key not in seen:
            seen.add(key)
            c = by_key[key]["data"]
            m = re.match(r"Chapter (\d+)", c["name"])
            if m:
                return int(m.group(1))
            key = c.get("parentCollection") or None
        return None

    return {k: resolve(k) for k in by_key}


def first_creator(data):
    for c in data.get("creators", []):
        return (c.get("lastName") or c.get("name") or "").strip()
    return ""


def year_of(data):
    m = re.search(r"(\d{4})", data.get("date", "") or "")
    return m.group(1) if m else ""


def main():
    print("Fetching collections...")
    collections = fetch_all("collections", "format=json")
    coll_chapter = chapter_of_collection(collections)

    print("Fetching items...")
    raw = fetch_all("items/top", f"format=json&include=data,bib&style={STYLE}&linkwrap=1")

    records = []
    for it in raw:
        data = it["data"]
        if data.get("itemType") in ("attachment", "note"):
            continue
        chapters = sorted({coll_chapter[c] for c in data.get("collections", [])
                           if coll_chapter.get(c) is not None})
        doi = data.get("DOI", "")
        url = data.get("url", "") or (f"https://doi.org/{doi}" if doi else "")
        bib = it.get("bib", "")
        # Strip the wrapper <div class="csl-bib-body"> ... <div class="csl-entry"> ... </div></div>
        bib = re.sub(r'^\s*<div class="csl-bib-body"[^>]*>\s*', "", bib)
        bib = re.sub(r'\s*</div>\s*$', "", bib)
        bib = re.sub(r'<div class="csl-entry"[^>]*>', "", bib)
        bib = re.sub(r"</div>", "", bib).strip()
        title = data.get("title") or data.get("bookTitle") or data.get("websiteTitle") or "(untitled)"
        records.append({
            "key": it["key"],
            "title": html.unescape(title),
            "year": year_of(data),
            "sort": (first_creator(data) + " " + title).lower(),
            "type": data.get("itemType", ""),
            "url": url,
            "zotero": f"https://www.zotero.org/groups/{GROUP_ID}/oue/items/{it['key']}",
            "bib": bib,
            "chapters": chapters,
        })

    records.sort(key=lambda r: r["sort"])
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(records, fh, ensure_ascii=False, indent=1)
    cited = sum(1 for r in records if r["chapters"])
    print(f"Wrote {len(records)} items to {OUT} ({cited} assigned to a chapter).")


if __name__ == "__main__":
    main()
