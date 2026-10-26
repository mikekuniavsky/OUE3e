---
title: Chapters
nav_order: 2
has_children: true
permalink: /chapters/
---

# Chapters

The book has 19 chapters. Each page here gives you a short description, how the chapter is organized, its keywords, the links we printed in it, and some further reading from our Zotero library. For the chapter itself, you'll need the book.

<table>
  <thead>
    <tr><th>#</th><th>Chapter</th><th>What it's about</th></tr>
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
