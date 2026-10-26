---
title: About
nav_order: 5
permalink: /about/
---

# About the book and this site

*Observing the User Experience* is a guide to the methods of user research. It's for researchers, and for anyone else who needs to understand the people they're designing for: designers, product managers, engineers, founders. This is the companion site for the third edition.

## Who we are

{% for a in site.data.authors %}
- {% include author.html name=a.name %}
{%- endfor %}

We wrote this edition together. Mike wrote the first edition on his own, and the second edition had a third author, Andrea Moed.

## What's here

- [Chapters]({{ '/chapters/' | relative_url }}): a short guide to each of the 19 chapters.
- [Bibliography]({{ '/bibliography/' | relative_url }}): the sources we collected, from our shared Zotero library.
- [Resources]({{ '/resources/' | relative_url }}): the links and tools we mention in the chapters.

## What isn't

The chapter text. For that you'll need the book, which you can get from [Elsevier]({{ site.data.book.elsevier }}) or [Amazon US]({{ site.data.book.amazon_us }}). This site only describes it and points to other things worth reading.

## Corrections

Found a dead link, a missing source or a mistake? [Open an issue on GitHub](https://github.com/mikekuniavsky/OUE3e/issues) and we'll fix it. The site's code and data are in [that repository](https://github.com/mikekuniavsky/OUE3e) too.
