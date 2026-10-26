---
title: Home
layout: home
nav_order: 1
description: Companion site for Observing the User Experience, third edition
permalink: /
---

# Observing the User Experience
{: .fs-9 }

A practitioner's guide to user research, third edition, by Elizabeth Goodman and Mike Kuniavsky.
{: .fs-6 .fw-300 }

[Browse the chapters]({{ '/chapters/' | relative_url }}){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Search the bibliography]({{ '/bibliography/' | relative_url }}){: .btn .fs-5 .mb-4 .mb-md-0 }

---

This site accompanies the book. It does not reproduce the book's text. It gives you:

- **A guide to each chapter:** what it covers, its main sections and key terms, so you can find the right method quickly.
- **A bibliography:** the sources behind the book, searchable and grouped by chapter, drawn from the book's [Zotero library](https://www.zotero.org/groups/5691168/oue/library).
- **Resources:** the web links and tools mentioned in the chapters, in one place.

{: .note }
This is a work in progress. Chapter descriptions and links will change as the book moves to print.

## The book at a glance

User experience research is the process of figuring out how an audience interprets and uses a designed artifact: an app, a medical device, a service. The book starts with planning (programs, projects, recruiting, desk research), moves through the main ways of learning from people (interviews, observation, usability tests, surveys, diaries, groups, findability methods), shows how to analyze and represent what you learn (qualitative analysis; personas, processes and systems), and ends with sharing it, running research as an operation, and using it to change the organization.

<div class="chapter-grid">
{%- for c in site.data.chapters %}
  <a class="chapter-card" href="{{ '/chapters/' | append: c.slug | append: '/' | relative_url }}">
    <span class="chapter-num">{{ c.num }}</span>
    <span class="chapter-title">{{ c.title }}</span>
  </a>
{%- endfor %}
</div>
