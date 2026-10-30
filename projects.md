---
layout: page
title: Projects
permalink: /projects/
---
Things I've built and am building.

{% assign sorted = site.projects | sort: "year" | reverse %}
{% for p in sorted %}
### [{{ p.title }}]({{ p.url | relative_url }})
{{ p.year }}{% if p.status %} · {{ p.status }}{% endif %}{% if p.tags %} · {{ p.tags | join: ", " }}{% endif %}

{{ p.summary }}

{% if p.repo %}[Code]({{ p.repo }}){% endif %}{% if p.repo and p.demo %} · {% endif %}{% if p.demo %}[Demo]({{ p.demo }}){% endif %}

{% endfor %}
