from flask import request
from flask import make_response
from flask import render_template
from flask import redirect
from datetime import datetime, timedelta
import requests
import urllib.parse
import json
from minsocial.auth import login_required

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

with open("config.json", "r", encoding="utf-8") as config_file:
        configs = json.loads(config_file.read())

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route("/home")
@login_required
def home():
    a = request.cookies.get("access_token")
    user_id = request.cookies.get("id")
        
    url = "https://api.twitter.com/2/users/{}/mentions".format(user_id)
    headers = {
        "Authorization" : "Bearer {}".format(a)
    }

    r = requests.get(url, headers=headers)

    mentions = r.json()["data"]

    return render_template("index.html", mentions=mentions)

@bp.route("/dm")
@login_required
def dm():
    a = request.cookies.get("access_token")
    user_id = request.cookies.get("id")
        
    url = "https://api.twitter.com/2/dm_events?dm_event.fields=id,text,sender_id".format(user_id)
    headers = {
        "Authorization" : "Bearer {}".format(a)
    }

    r = requests.get(url, headers=headers)
    dms = r.json()["data"]

    data = []
    for dm in dms:
        dm_details = {}
        dm_details["text"] = dm["text"]

        new_url = "https://api.twitter.com/2/users/{}".format(dm["sender_id"])
        r2 = requests.get(new_url, headers=headers)

        sender_det = r2.json()["data"]["username"]
        dm_details["sender_name"] = sender_det

        new_url = "https://api.twitter.com/2/users/{}".format(dm["sender_id"])
        r2 = requests.get(new_url, headers=headers)

        sender_det = r2.json()["data"]["username"]

        data.append(dm_details)


    return render_template("dms.html", dms=data)