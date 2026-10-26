---
title: Resources
nav_order: 4
permalink: /resources/
---

# Resources

Web links and tools mentioned in the chapters, collected in one place. Links are as printed in the manuscript; some may have changed.

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
<p><strong>Tools and organizations named:</strong> {{ c.tools | join: ", " }}.</p>
{%- endif %}
{%- endif %}
{%- endfor %}
