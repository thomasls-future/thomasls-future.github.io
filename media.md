---
layout: page
title: Current Media
permalink: /media/
---
<p class="jump"><a href="#music">Music</a> · <a href="#film">Film</a> · <small>Updated {{ site.time | date: "%b %-d, %Y" }}</small></p>

## Music {#music}
<p class="more"><a href="https://www.last.fm/user/thomas_1972">All listening on Last.fm →</a></p>
<ul class="tracks">
{% for t in site.data.lastfm_recent limit:8 %}
  <li>
    {% if t.art != "" %}<img src="{{ t.art }}" alt="" loading="lazy" width="64" height="64">{% else %}<span class="noart"></span>{% endif %}
    <div>
      <a href="{{ t.url }}"><strong>{{ t.name }}</strong></a><br>
      {{ t.artist }}{% if t.album != "" %} · {{ t.album }}{% endif %}<br>
      <small>{% if t.now_playing %}Now playing{% else %}{{ t.played | date: "%b %-d" }}{% endif %}</small>
    </div>
  </li>
{% endfor %}
</ul>

## Film {#film}
<p class="more"><a href="https://letterboxd.com/thomasls/">All films on Letterboxd →</a></p>
{% assign recent = site.data.letterboxd | slice: 0, 24 %}
{% assign months = recent | group_by_exp: "f", "f.watched | slice: 0, 7" %}
{% for m in months %}
### {{ m.name | append: "-01" | date: "%B %Y" }}
<div class="films">
{% for f in m.items %}
  <a href="{{ f.link }}" class="film">
    {% if f.poster != "" %}<img src="{{ f.poster }}" alt="{{ f.title }} poster" loading="lazy">{% endif %}
    <span class="film-title">{{ f.title }} ({{ f.year }})</span>
    <small>{{ f.stars }}{% if f.stars != "" %} · {% endif %}{{ f.watched | date: "%b %-d" }}</small>
  </a>
{% endfor %}
</div>
{% endfor %}
