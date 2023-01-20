from flask import request
from flask import make_response
from flask import render_template
from flask import redirect
from datetime import datetime, timedelta
import requests
import urllib.parse
import json
from minsocial.decorators import login_required
from minsocial import constants

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route("/home")
@login_required
def home():
    a = request.cookies.get("access_token")
    user_id = request.cookies.get("id")
        
    url = constants.GET_MENTIONED["URL"].format(user_id)
    headers = constants.GET_MENTIONED["HEADER"].copy()
    headers["Authorization"] = headers["Authorization"].format(a)

    r = requests.get(url, headers=headers)

    mentions = r.json().get("data")

    return render_template("index.html", mentions=mentions)

@bp.route("/dm")
@login_required
def dm():
    a = request.cookies.get("access_token")
    user_id = request.cookies.get("id")
        
    url = constants.GET_DMS["URL"]
    headers = constants.GET_DMS["HEADER"].copy()
    headers["Authorization"] = headers["Authorization"].format(a)

    r = requests.get(url, headers=headers)
    dms = r.json()["data"]

    data = []
    for dm in dms:
        dm_details = {}
        dm_details["text"] = dm["text"]

        # Convert to cache retrieval
        new_url = constants.GET_USER["URL"].format(dm["sender_id"])
        r2 = requests.get(new_url, headers=headers)

        sender_det = r2.json()["data"]["username"]
        dm_details["sender_name"] = sender_det

        new_url = constants.GET_USER["URL"].format(dm["sender_id"])
        r2 = requests.get(new_url, headers=headers)

        sender_det = r2.json()["data"]["username"]

        data.append(dm_details)


    return render_template("dms.html", dms=data)


@bp.route("/tweet/<tweet_id>")
@login_required
def view_tweet(tweet_id): # ADD MORE DETAILS
    a = request.cookies.get("access_token")

    url = constants.GET_TWEET["URL"].format(tweet_id)
    headers = constants.GET_DMS["HEADER"].copy()
    headers["Authorization"] = headers["Authorization"].format(a)

    r = requests.get(url, headers=headers)
    tweet_details = r.text

    return tweet_details

@bp.route("/compose", methods=['GET', 'POST'])
@login_required
def compose_tweet():
    if request.method == "GET":
        return redirect(url_for("home.home"))

    if request.form["text"] == None:
        return redirect(url_for("home.home"))

    dataToSend = {
        "text": request.form["text"]
    }

    headers = {
        "Authorization" : "Bearer {}".format(request.cookies.get("access_token")),
        "Content-Type": "application/json"
    }
    
    URL = "https://api.twitter.com/2/tweets"

    r = requests.post(URL, headers=headers, json=dataToSend)

    print(r.text)

    if r.status_code == 201:
        data = r.json()["data"]
        print(data)
        return redirect(url_for('home.view_tweet', tweet_id=data["id"]))

    return redirect(url_for("home.home"))