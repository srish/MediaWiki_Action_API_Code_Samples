#This file is partly auto-generated

#!/usr/bin/python3

"""
    get_filtered_page_revisions.py

    MediaWiki Action API Code Samples
    Demo of `Revisions` module: Get data including content of last 5 revisions
    of the title [[API:Geosearch]] made after the 1st of July 2018 i.e 2018-07-01
    excluding changes made by the user SSethi (WMF)

    MIT License
"""

import requests

S = requests.Session()

URL = "https://mediawiki.org/w/api.php"

PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "API:Geosearch",
    "rvlimit": "5",
    "rvprop": "timestamp|user|comment|content",
    "rvdir": "newer",
    "rvstart": "2018-07-01T00:00:00Z",
    "rvexcludeuser": "SSethi (WMF)",
    "rvslots": "main",
    "formatversion": "2",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
