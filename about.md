---
title: About
nav_order: 5
permalink: /about/
---

# About the book and this site

*Observing the User Experience* is a guide to the methods of user experience research, for researchers and for everyone who needs to understand the people they design for: designers, product managers, engineers and founders. This is the companion site for the third edition.

## Authors

**Elizabeth Goodman** and **Mike Kuniavsky** wrote the third edition. Earlier editions were co-written with Andrea Moed.

## What is on this site

- [Chapters]({{ '/chapters/' | relative_url }}): an overview of each of the 19 chapters.
- [Bibliography]({{ '/bibliography/' | relative_url }}): sources collected for the book, from its shared Zotero library.
- [Resources]({{ '/resources/' | relative_url }}): links and tools mentioned in the chapters.

## What is not here

The chapter text. The book is published by Elsevier; read it there. This site only summarizes and points to other material.

## How the site is built

The site is built with Jekyll and the Just the Docs theme and is published through GitHub Pages. Chapter overviews come from `_data/chapters.yml`. The bibliography comes from the book's public Zotero library: the script `scripts/fetch_zotero.py` downloads it into `_data/zotero.json`. See the repository's README for how to update either one.

## Corrections and suggestions

If you find a broken link, a missing source or a mistake, please open an issue in the [GitHub repository](https://github.com/mikekuniavsky/OUE3e).
