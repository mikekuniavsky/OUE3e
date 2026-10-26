---
title: Resources
nav_order: 4
permalink: /resources/
---

# Resources

The links and tools we mention in the chapters, all in one place. These are the links as we wrote them, so some may have gone stale. If you find one, tell us.

{%- for c in site.data.chapters %}
{%- if c.links.size > 0 or c.tools.size > 0 %}

## Chapter {{ c.num }}: {{ c.title }}
{: .no_toc }

{%- if c.links.size > 0 %}
<ul>
{%- for l in c.links %}
  <li><a href="{{ l.url }}">{{ l.label }}</a></li>
{%- endfor %}
</ul>
{%- endif %}
{%- if c.tools.size > 0 %}
<p><strong>Tools and companies we mention:</strong> {{ c.tools | join: ", " }}.</p>
{%- endif %}
{%- endif %}
{%- endfor %}
