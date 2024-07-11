---
title: All Typos
published: true
sidebar: mydoc_sidebar
permalink: alltypos.html
folder: monograph
---

{% paginate pages by 2 -%}
  {% for page in pages -%}
    {{ page.title | link_to: page.url }}
  {%- endfor %}

  {{- paginate | default_pagination }}
{%- endpaginate %}