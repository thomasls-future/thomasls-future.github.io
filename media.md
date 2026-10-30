---
layout: page
title: Current Media
permalink: /media/
---
## Recently played
<ul class="tracks">
{% for t in site.data.lastfm_recent limit:10 %}
  <li>
    {% if t.art != "" %}<img src="{{ t.art }}" alt="" loading="lazy" width="64" height="64">{% else %}<span class="noart"></span>{% endif %}
    <div>
      <a href="{{ t.url }}"><strong>{{ t.name }}</strong></a><br>
      {{ t.artist }}{% if t.album != "" %} · {{ t.album }}{% endif %}<br>
      <small>{% if t.now_playing %}Now playing{% else %}{{ t.played | date: "%b %-d, %Y" }}{% endif %}</small>
    </div>
  </li>
{% endfor %}
</ul>

## Recently watched
<div class="films">
{% for f in site.data.letterboxd limit:12 %}
  <a href="{{ f.link }}" class="film">
    {% if f.poster != "" %}<img src="{{ f.poster }}" alt="{{ f.title }} poster" loading="lazy">{% endif %}
    <span class="film-title">{{ f.title }} ({{ f.year }})</span>
    <small>{% if f.rating %}{{ f.rating }} · {% endif %}{{ f.watched | date: "%b %-d, %Y" }}</small>
  </a>
{% endfor %}
</div>
