---
title: All Typos
published: true
sidebar: mydoc_sidebar
permalink: alltypos.html
folder: monograph
---

hello4!

{% assign files = site.pages | where: "folder", "monograph" %}
  {% for file in files %}
    {% if file.extname == "Introduction.md" %}
    {{ file.content }}
    {% endif %}
  {% endfor %}