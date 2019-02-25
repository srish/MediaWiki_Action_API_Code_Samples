#!/usr/bin/python3

"""
    undelete.py

    MediaWiki Action API Code Samples
    Demo of `Undelete` module: POST request to restore a page
    MIT license
"""

import requests

S = requests.Session()

URL = "http://dev.wiki.local.wmftest.net:8080/w/api.php"

# Step 1: GET Request to fetch login token
PARAMS_0 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step 2: POST Request to log in. Use of main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_1 = {
    "action": "login",
    "lgname": "your_bot_username",
    "lgpassword": "your_bot_password",
    "lgtoken": LOGIN_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_1)

# Step 3: GET request to fetch CSRF token
PARAMS_2 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

# Step 4: POST request to restore a page
PARAMS_3 = {
    "action": "undelete",
    "title": "page_title",
    "reason": "reason",
    "token": CSRF_TOKEN,
    "format": "json",
}

R = S.post(URL, data=PARAMS_3)
DATA = R.json()

print(DATA)