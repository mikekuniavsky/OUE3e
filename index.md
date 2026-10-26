---
title: Home
layout: home
nav_order: 1
description: Companion site for Observing the User Experience, third edition
permalink: /
---

# Observing the User Experience
{: .fs-9 }

Third edition, by {% include authors.html %}
{: .fs-6 .fw-300 }

[Browse the chapters]({{ '/chapters/' | relative_url }}){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Get the book]({{ '/#get-the-book' | relative_url }}){: .btn .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Search the bibliography]({{ '/bibliography/' | relative_url }}){: .btn .fs-5 .mb-4 .mb-md-0 }

---

This site goes with the book. It doesn't contain the book (that's what the book is for). Here's what it does have:

- **A guide to each chapter,** so you can find the method you need.
- **Our bibliography,** sorted by chapter and searchable. It comes from our [Zotero library](https://www.zotero.org/groups/5691168/oue/library).
- **The links and tools we mention,** all in one place.

## Get the book

You can buy it from [Elsevier]({{ site.data.book.elsevier }}) or from [Amazon US]({{ site.data.book.amazon_us }}).

{: .note }
We're still building this. Descriptions and links will change as the book goes to print.

## What the book covers

User research means finding out how people understand and use something somebody designed: an app, a medical device, a service. The first chapters are about planning, recruiting, and what's already known. Then come the ways of learning from people: interviews, visits, usability tests, surveys, diaries, groups, and tests for whether people can find things. The rest is about making sense of what you learned, showing it to other people, running research as an operation, and getting your organization to do something about it.

<div class="chapter-grid">
{%- for c in site.data.chapters %}
  <a class="chapter-card" href="{{ '/chapters/' | append: c.slug | append: '/' | relative_url }}">
    <span class="chapter-num">{{ c.num }}</span>
    <span class="chapter-title">{{ c.title }}</span>
  </a>
{%- endfor %}
</div>
