---
title: Chapters
nav_order: 2
has_children: true
permalink: /chapters/
---

# Chapters

The book has 19 chapters. Each page here gives a short overview, the main sections, key terms, any links printed in the chapter, and further reading from the book's Zotero library. The chapter text itself is in the book.

<table>
  <thead>
    <tr><th>#</th><th>Chapter</th><th>What it covers</th></tr>
  </thead>
  <tbody>
  {%- for c in site.data.chapters %}
    <tr>
      <td>{{ c.num }}</td>
      <td><a href="{{ '/chapters/' | append: c.slug | append: '/' | relative_url }}">{{ c.title }}</a></td>
      <td>{{ c.summary | truncatewords: 22 }}</td>
    </tr>
  {%- endfor %}
  </tbody>
</table>
