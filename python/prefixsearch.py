#This file is partly auto-generated

#!/usr/bin/python3

"""
    prefixsearch.py

    MediaWiki Action API Code Samples
    Demo of `Prefixsearch` module: Perform a prefix search for page titles

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "prefixsearch",
    "pssearch": "Star Wars"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
