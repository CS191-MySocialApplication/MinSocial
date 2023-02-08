from flask import (
    make_response, redirect, render_template, request, Blueprint, url_for
)

import requests
import urllib.parse
import json

with open("config.json", "r", encoding="utf-8") as config_file:
    configs = json.loads(config_file.read())

bp = Blueprint('mstdnauth', __name__, url_prefix='/mstdn/')

@bp.route("/")
def log_in():
    
    url = "https://social.up.edu.ph/oauth/authorize?"
    parameters = {"response_type":"code",
    "client_id": configs["mastodon_client_id"],
    "redirect_uri":"http://127.0.0.1:5000/mstdn/logged",
    "scope":"read write follow",
    "force_login":"true"}

    authlink = url + urllib.parse.urlencode(parameters)

    return render_template('login.html', authlink=authlink)

@bp.route("/logged", methods=['GET'])
def logged():
    code = request.args["code"]
    
    url = "https://social.up.edu.ph/oauth/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    dataToSend = {
        "code": code,
        "grant_type":"authorization_code",
        "client_id": configs["mastodon_client_id"],
        "client_secret": configs["mastodon_client_secret"],
        "redirect_uri": "http://127.0.0.1:5000/mstdn/logged",
        "scope":"read write follow"
    }
    
    r = requests.post(url, headers=headers, data=dataToSend)
    token = r.json()

    print(token)

    resp = make_response(redirect(url_for("mstdn.home")))
    resp.set_cookie("mstdn_access_token", token["access_token"], max_age=3600)
    
    return resp

@bp.route("/logout")
def logout():
    a = request.cookies.get("mstdn_access_token")

    url = "https://social.up.edu.ph/oauth/revoke"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    if a is not None:

        dataToSend = {
            "client_id": configs["mastodon_client_id"],
            "client_secret": configs["mastodon_client_secret"],
            "token":a,
        }

        r = requests.post(url, headers=headers, data=dataToSend)

    resp = make_response(redirect("/"))
    resp.set_cookie("access_token", "", expires=0)

    return resp