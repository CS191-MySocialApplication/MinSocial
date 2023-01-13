from flask import request
from flask import make_response
from flask import render_template
from flask import redirect
from datetime import datetime, timedelta
import requests
import urllib.parse
import json


from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


with open("config.json", "r", encoding="utf-8") as config_file:
        configs = json.loads(config_file.read())

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route("/home")
def home():
    a = request.cookies.get("access_token")
    b = request.cookies.get("refresh_token")
    user_id = request.cookies.get("id")

    if a == None:
        url = "https://api.twitter.com/2/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        
        dataToSend = {
            "refresh_token": b,
            "grant_type":"refresh_token",
            "client_id": configs["twitter_client_id"],

        }

        r = requests.post(url, headers=headers, data=dataToSend)
        token = r.json()
        a = token["access_token"]
        
    url = "https://api.twitter.com/2/users/{}/mentions".format(user_id)
    headers = {
        "Authorization" : "Bearer {}".format(a)
    }

    r = requests.get(url, headers=headers)
    mentions = r.json()["data"]

    return render_template("index.html", mentions=mentions)

@bp.route("/dm")
def dm():
    a = request.cookies.get("access_token")
    b = request.cookies.get("refresh_token")
    user_id = request.cookies.get("id")

    if a == None:
        url = "https://api.twitter.com/2/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        
        dataToSend = {
            "refresh_token": b,
            "grant_type":"refresh_token",
            "client_id": configs["twitter_client_id"],

        }

        r = requests.post(url, headers=headers, data=dataToSend)
        token = r.json()
        a = token["access_token"]
        
    url = "https://api.twitter.com/2/dm_events?dm_event.fields=id,text,sender_id".format(user_id)
    headers = {
        "Authorization" : "Bearer {}".format(a)
    }

    r = requests.get(url, headers=headers)
    print(r.text)
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