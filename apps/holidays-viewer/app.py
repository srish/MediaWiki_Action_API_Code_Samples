#!/usr/bin/python3

"""
    app.py

    MediaWiki API Demos

    Holidays viewer: A demo app that fetches the day's holidays from Wikipedia
    with options to search for holidays of other dates, and login to add new
    holidays.

    MIT license
"""

from datetime import datetime
from flask import Flask, render_template, flash, request, url_for, redirect
import requests


APP = Flask(__name__)
APP.secret_key = 'your_secret_key'

URL = "https://en.wikipedia.org/w/api.php"
TEST_URL = "https://test.wikipedia.org/w/api.php"
TEST_PAGE = "Sandbox/Holidays_and_observances"
S = requests.Session()
IS_LOGGED_IN = False

@APP.route('/', methods=['GET', 'POST'])
@APP.route('/<holidays_date>', methods=['GET', 'POST'])
def list_holidays(holidays_date=None):
    """ Lists holidays for the current date or a custom date
    """

    if holidays_date is None:
        holidays_date = get_todays_date()

    # Update date to a custom date
    if request.method == 'POST' and 'search' in request.form:
        search_month = str(request.form.get('monthList'))
        search_day = str(request.form.get('dayList'))
        holidays_date = search_month +"_"+search_day

    # Get the section numbers for the holidays on Wikipedia and for those on the test page
    section_number = get_holidays_section(URL, holidays_date, None)
    test_section_number = get_holidays_section(TEST_URL, TEST_PAGE, holidays_date)

    holidays = get_holidays(URL, holidays_date, section_number)
    test_holidays = get_holidays(TEST_URL, TEST_PAGE, test_section_number)

    holidays_html = test_holidays + holidays
    flash('Holidays added through this app are in bold')

    return render_template("index.html", header=holidays_date.replace('_', ' '),
                           holidays_html=holidays_html)


def get_todays_date():
    """ Get the current month as text and the current day as a number
    """

    current_month = datetime.now().strftime('%B')
    current_day = datetime.now().strftime('%d')
    if current_day.startswith('0'):
        current_day = current_day.replace('0', '')

    return current_month + "_" + current_day

def get_holidays_section(url, page, date_to_get):
    """ Get the section number for holidays on Wikipedia and holidays on the test page
    """

    params = {
        "format":"json",
        "action":"parse",
        "prop":"sections",
        "page":page
    }

    response = S.get(url=url, params=params)
    data = response.json()
    sections = data['parse']['sections']
    section_number = "0"

    for index, value in enumerate(sections):
        if value['anchor'] == "Holidays_and_observances":
            section_number = index + 1

        if url == TEST_URL:
            if value['anchor'] == date_to_get:
                section_number = index + 1

    return section_number

def get_holidays(url, page, section_number):
    """ Get the html which contains holidays
    """

    params = {
        "format":"json",
        "action":"parse",
        "prop":"text",
        "page": page,
        "section": section_number,
        "disableeditsection":1
    }

    response = S.get(url=url, params=params)
    data = response.json()
    text = data['parse']['text']['*']

    return text

@APP.route("/search")
def search():
    """ Search for holidays of custom dates
    """

    return render_template("search.html", header="Search date")

@APP.route("/login", methods=['GET', 'POST'])
def login():
    """ Login to Wikipedia
    """

    if request.method == 'POST' and 'login' in request.form:
        params_0 = {
            "action": "query",
            "meta": "tokens",
            "type": "login",
            "format": "json"
        }

        response = S.get(url=URL, params=params_0)
        data = response.json()

        login_token = data['query']['tokens']['logintoken']

        params_1 = {
            "action": "clientlogin",
            "username": str(request.form.get('username')),
            "password": str(request.form.get('password')),
            "loginreturnurl": "http://127.0.0.1:5000/login",
            "logintoken": login_token,
            "format": "json"
        }

        response = S.post(url=URL, data=params_1)
        data = response.json()

        if data['clientlogin']['status'] != 'PASS':
            flash('Oops! Something went wrong -- ' + data['clientlogin']['messagecode'])
        else:
            global IS_LOGGED_IN
            IS_LOGGED_IN = True
            flash('Login success! Welcome, ' + data['clientlogin']['username'] + '!')
            return redirect(url_for('add'))

    return render_template("login.html", header="Login")

@APP.route("/add", methods=['GET', 'POST'])
def add():
    """ Add a new holiday to a test page and redirect to that date's holidays
        to show the added holidays
    """

    if not IS_LOGGED_IN:
        return redirect(url_for('login'))

    if request.method == 'POST' and 'add' in request.form:

        # Wiki markup to format the added holiday's text as a list item and in bold
        holiday_text = "* '''" + str(request.form.get('description')) + "'''"
        date = str(request.form.get('date'))

        params_2 = {
            "action": "query",
            "meta": "tokens",
            "format": "json"
        }

        response = S.get(url=TEST_URL, params=params_2)
        data = response.json()

        csrf_token = data['query']['tokens']['csrftoken']

        params_4 = {
            "action": "edit",
            "title": TEST_PAGE,
            "token": csrf_token,
            "format": "json",
            "section": "new",
            "sectiontitle": date,
            "text": holiday_text,
        }

        response = S.post(url=TEST_URL, data=params_4)
        data = response.json()

        if data['edit']['result'] != 'Success':
            flash('Oops! Something went wrong -- ' + data['clientlogin']['messagecode'])
        else:
            flash('New holiday added successfully!')
            return redirect(url_for('list_holidays', holidays_date=date.replace(' ', '_')))

    return render_template("add.html", header="Add holiday")

if __name__ == "__main__":
    APP.run()
