import json, os, re, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone

LFM_USER = "thomas_1972"
LB_USER = "thomasls"

# Last.fm's generic "no art" placeholder
LFM_PLACEHOLDER = "2a96cbd8b46e442fc41c2b86b821562f"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "media-sync"})
    return urllib.request.urlopen(req, timeout=30).read()

def save(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=1)

try:
    lfm = json.loads(get(
        "https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks"
        f"&user={LFM_USER}&api_key={os.environ['LASTFM_KEY']}&format=json&limit=20"))
    tracks = []
    for t in lfm["recenttracks"]["track"]:
        imgs = {i["size"]: i["#text"] for i in t.get("image", [])}
        art = imgs.get("extralarge") or imgs.get("large") or ""
        if LFM_PLACEHOLDER in art:
            art = ""
        uts = (t.get("date") or {}).get("uts")
        tracks.append({
            "artist": t["artist"]["#text"],
            "name": t["name"],
            "album": t["album"]["#text"],
            "art": art,
            "url": t["url"],
            "now_playing": t.get("@attr", {}).get("nowplaying") == "true",
            "played": datetime.fromtimestamp(int(uts), timezone.utc).isoformat() if uts else None,
        })
    save("_data/lastfm_recent.json", tracks)
except Exception as e:
    print("Last.fm fetch failed:", e)

try:
    ns = {"lb": "https://letterboxd.com"}
    root = ET.fromstring(get(f"https://letterboxd.com/{LB_USER}/rss/"))
    films = []
    for i in root.iter("item"):
        if i.find("lb:filmTitle", ns) is None:
            continue
        m = re.search(r'<img src="([^"]+)"', i.findtext("description") or "")
        films.append({
            "title": i.findtext("lb:filmTitle", namespaces=ns),
            "year": i.findtext("lb:filmYear", namespaces=ns),
            "rating": i.findtext("lb:memberRating", namespaces=ns),
            "watched": i.findtext("lb:watchedDate", namespaces=ns),
            "rewatch": i.findtext("lb:rewatch", namespaces=ns) == "Yes",
            "poster": m.group(1) if m else "",
            "link": i.findtext("link"),
        })
    save("_data/letterboxd.json", films)
except Exception as e:
    print("Letterboxd fetch failed:", e)
