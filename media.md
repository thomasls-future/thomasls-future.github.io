---
layout: page
title: Current Media
permalink: /media/
---
## Recently played
{% for t in site.data.lastfm_recent limit:10 %}
- {{ t.artist["#text"] }} – {{ t.name }}
{% endfor %}

## Recently watched
{% for f in site.data.letterboxd limit:10 %}
- [{{ f.title }}]({{ f.link }}) ({{ f.year }}) {{ f.rating }}
{% endfor %}
