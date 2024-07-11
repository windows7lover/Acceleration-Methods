---
title: All Typos
published: true
sidebar: mydoc_sidebar
permalink: alltypos.html
folder: monograph
---

hello5

{% assign files = site.pages %}
  {% for file in files %}
    {% if file.extname == "Introduction.md" %}
    {{ file.content }}
    {% endif %}
  {% endfor %}