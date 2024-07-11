---
title: All Typos
published: true
sidebar: mydoc_sidebar
permalink: alltypos.html
folder: monograph
---

# Aggregate Page

{% assign sorted_pages = site.monographtypos %}
{% for page in sorted_pages %}
  {{ page.content }}
{% endfor %}
