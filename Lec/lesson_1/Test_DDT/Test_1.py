# https://www.mediawiki.org/wiki/API:Geosearch
# Exempl 2. Редактируем код для теста.

import requests
S = requests.Session()

def get_sites(lat, long, radius, limit=100):
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "format": "json",
        "list": "geosearch",
        "gscoord": f"{lat}|{long}",
        "gslimit": f"{limit}",
        "gsradius": f"{radius}",
        "action": "query"
    }
    r = S.get(url=URL, params=PARAMS)
    pages = r.json()['query']['geosearch']
    sites = [i["title"] for i in pages]
    return sites

def test_step1(): # Ищем достопремичательность, башную по данным коордетнатам
    assert "One Montgomery Tower" in get_sites("37.7891838", "-122.4033522", 100), "NOTE FAUND"

#test_step1()