---
title: All Typos
published: true
sidebar: mydoc_sidebar
permalink: alltypos.html
folder: monograph
---

{% assign files = site.static_files | where: "path", "/pages/monograph" %}
{% for file in files %}
  {% if file.extname == ".md" %}
    {% capture file_content %}
      {{ file.content }}
    {% endcapture %}

    {% assign content_lines = file_content | split: "\n" %}
    {% assign start_index = content_lines.size %}

    {% for line in content_lines %}
      {% if line contains "---" %}
        {% assign start_index = forloop.index0 | plus: 1 %}
      {% endif %}
    {% endfor %}

    {% assign content = content_lines | slice: start_index, content_lines.size | join: "\n" %}

    {{ content | markdownify }}
  {% endif %}
{% endfor %}