---
layout: page
title: Projects
permalink: /projects/
---
{% for p in site.projects %}
- [{{ p.title }}]({{ p.url }}){% if p.summary %}: {{ p.summary }}{% endif %}
{% endfor %}
