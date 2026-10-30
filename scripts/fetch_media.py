import json, os, urllib.request, xml.etree.ElementTree as ET

LFM_USER = "thomasls.1972"
LB_USER = "thomasls"

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
    save("_data/lastfm_recent.json", lfm["recenttracks"]["track"])
except Exception as e:
    print("Last.fm fetch failed:", e)

try:
    ns = {"lb": "https://letterboxd.com"}
    root = ET.fromstring(get(f"https://letterboxd.com/{LB_USER}/rss/"))
    films = [{
        "title": i.findtext("lb:filmTitle", namespaces=ns),
        "year": i.findtext("lb:filmYear", namespaces=ns),
        "rating": i.findtext("lb:memberRating", namespaces=ns),
        "watched": i.findtext("lb:watchedDate", namespaces=ns),
        "link": i.findtext("link"),
    } for i in root.iter("item") if i.find("lb:filmTitle", ns) is not None]
    save("_data/letterboxd.json", films)
except Exception as e:
    print("Letterboxd fetch failed:", e)
