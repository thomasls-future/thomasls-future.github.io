---
layout: page
title: Current Media
permalink: /media/
---
## Listening
<div class="tiles tracks">
{% for t in site.data.lastfm_recent limit:8 %}
  <a href="{{ t.url }}" class="tile">
    {% if t.art != "" %}<img src="{{ t.art }}" alt="{{ t.album }} cover" loading="lazy">{% else %}<span class="noart"></span>{% endif %}
    <span class="tile-title">{{ t.name }}</span>
    <small>{{ t.artist }}</small>
    <small>{% if t.now_playing %}Now playing{% else %}{{ t.played | date: "%b %-d" }}{% endif %}</small>
  </a>
{% endfor %}
</div>
<p class="more"><a href="https://www.last.fm/user/thomas_1972">More on Last.fm →</a></p>

## Watching
<div class="tiles films">
{% for f in site.data.letterboxd limit:8 %}
  <a href="{{ f.link }}" class="tile">
    {% if f.poster != "" %}<img src="{{ f.poster }}" alt="{{ f.title }} poster" loading="lazy">{% endif %}
    <span class="tile-title">{{ f.title }}</span>
    <small>{{ f.year }}</small>
    <small>{{ f.watched | date: "%b %-d" }}</small>
  </a>
{% endfor %}
</div>
<p class="more"><a href="https://letterboxd.com/thomasls/">More on Letterboxd →</a></p>
