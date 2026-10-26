---
title: Bibliography
nav_order: 3
permalink: /bibliography/
---

# Bibliography

These are the sources we collected for the book, from our shared [Zotero library](https://www.zotero.org/groups/5691168/oue/library), in APA style and alphabetical order. Use the filter box or the chapter menu to narrow the list.

<div class="bib-controls">
  <label for="bib-filter">Filter</label>
  <input type="search" id="bib-filter" placeholder="Search author, title, year" autocomplete="off">
  <label for="bib-chapter">Chapter</label>
  <select id="bib-chapter">
    <option value="">All chapters</option>
    <option value="0">Preface</option>
    {%- for c in site.data.chapters %}
    <option value="{{ c.num }}">{{ c.num }}. {{ c.title }}</option>
    {%- endfor %}
  </select>
  <span id="bib-count" aria-live="polite"></span>
</div>

<ul class="bib" id="bib-list">
{%- for r in site.data.zotero %}
  <li id="{{ r.key }}" data-chapters=",{{ r.chapters | join: ',' }},">
    {{ r.bib }}
    {%- if r.chapters.size > 0 %}
    <span class="bib-chapters">Chapters:
      {%- for n in r.chapters %}
        {%- if n == 0 %} Preface{% else %}
        {%- assign rc = site.data.chapters | where: "num", n | first %} <a href="{{ '/chapters/' | append: rc.slug | append: '/' | relative_url }}">{{ n }}</a>{% endif %}
        {%- unless forloop.last %},{% endunless %}
      {%- endfor %}
    </span>
    {%- endif %}
  </li>
{%- endfor %}
</ul>

<script>
(function () {
  var items = Array.prototype.slice.call(document.querySelectorAll('#bib-list li'));
  var box = document.getElementById('bib-filter');
  var sel = document.getElementById('bib-chapter');
  var count = document.getElementById('bib-count');
  function update() {
    var q = box.value.trim().toLowerCase();
    var ch = sel.value;
    var shown = 0;
    items.forEach(function (li) {
      var okText = !q || li.textContent.toLowerCase().indexOf(q) !== -1;
      var okCh = !ch || li.getAttribute('data-chapters').indexOf(',' + ch + ',') !== -1;
      var show = okText && okCh;
      li.hidden = !show;
      if (show) shown++;
    });
    count.textContent = shown + ' of ' + items.length + ' sources';
  }
  box.addEventListener('input', update);
  sel.addEventListener('change', update);
  update();
})();
</script>
