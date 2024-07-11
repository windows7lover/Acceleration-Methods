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
    {{ file.content }}
    {% endif %}
  {% endfor %}