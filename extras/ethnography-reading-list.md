---
title: Ethnography reading list
parent: Extras
nav_order: 8
permalink: /extras/ethnography-reading-list/
---

# Ethnography reading list

For [Chapter 7, Learning from Observation]({{ '/chapters/learning-from-observation/' | relative_url }}). If you want to understand what people do and why they do it, and you're ready to go deeper than the chapter does, start here.
{: .fs-5 }

Sam Ladner's *Practical Ethnography: A Guide to Doing Ethnography in the Private Sector* is the first place we send people.

{%- assign shown = 0 %}
<ul class="bib">
{%- for r in site.data.zotero %}
  {%- if r.chapters contains 7 %}
  {%- assign shown = shown | plus: 1 %}
  <li id="{{ r.key }}">{{ r.bib }}</li>
  {%- endif %}
{%- endfor %}
</ul>

These come from [our Zotero library](https://www.zotero.org/groups/5691168/oue/library). The full list for every chapter is in the [bibliography]({{ '/bibliography/' | relative_url }}).
