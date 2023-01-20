from flask import g
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from datetime import datetime, timedelta
import requests
import urllib.parse
import json


from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

with open("config.json", "r", encoding="utf-8") as config_file:
        configs = json.loads(config_file.read())

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.route("/")
def log_in():
    
    url = "https://twitter.com/i/oauth2/authorize?"
    parameters = {"response_type":"code",
    "client_id": configs["twitter_client_id"],
    "redirect_uri":"http://127.0.0.1:5000/logged",
    "scope":"tweet.read tweet.write users.read follows.read offline.access dm.read",
    "state":"state",
    "code_challenge":"challenge",
    "code_challenge_method":"plain"}

    authlink = url + urllib.parse.urlencode(parameters)

    return render_template('login.html', authlink=authlink)

@bp.route("/logged", methods=['GET'])
def logged():
    code = request.args["code"]
    
    url = "https://api.twitter.com/2/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    dataToSend = {
        "code": code,
        "grant_type":"authorization_code",
        "client_id": configs["twitter_client_id"],
        "redirect_uri": "http://127.0.0.1:5000/logged",
        "code_verifier": "challenge"
    }
    
    r = requests.post(url, headers=headers, data=dataToSend)
    token = r.json()

    url_me = "https://api.twitter.com/2/users/me"
    headers = {
        "Authorization" : "Bearer {}".format(token["access_token"])
    }

    r = requests.get(url_me, headers=headers)
    user_details = r.json()["data"]

    resp = make_response(redirect("/home"))
    resp.set_cookie("access_token", token["access_token"], max_age=3600)
    resp.set_cookie("refresh_token", token["refresh_token"], max_age=3600)
    resp.set_cookie("id", user_details["id"], max_age=60000*30) # BUG: WILL PERSIST EVEN WITH OTHER USERS
    resp.set_cookie("name", user_details["name"], max_age=60000*30)
    resp.set_cookie("username", user_details["username"], max_age=60000*30)

    return resp

@bp.route("/logout")
def logout():
    a = request.cookies.get("access_token")
    b = request.cookies.get("refresh_token")

    url = "https://api.twitter.com/2/oauth2/revoke"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    if a is not None:

        dataToSend = {
            "client_id": configs["twitter_client_id"],
            "token":a,
            "token_type_hint": "access_token"
        }

        r = requests.post(url, headers=headers, data=dataToSend)

    if b is not None:
        
        dataToSend = {
            "client_id": configs["twitter_client_id"],
            "token":b,
            "token_type_hint": "refresh_token"
        }

        r = requests.post(url, headers=headers, data=dataToSend)

    resp = make_response(redirect("/"))
    resp.set_cookie("access_token", "", expires=0)
    resp.set_cookie("refresh_token", "", expires=0)

    return resp