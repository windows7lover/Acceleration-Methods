---
title: All Typos
published: true
sidebar: mydoc_sidebar
permalink: alltypos.html
folder: monograph
---

{% assign files = site.pages | where: "folder", "monograph" %}
{% for file in files %}
{% if file.extname == ".md" %}
  {{ page.content }}
{% endif %}
{% endfor %}