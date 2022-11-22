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

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.route("/")
def log_in():


    url = "https://twitter.com/i/oauth2/authorize?"
    parameters = {"response_type":"code",
    "client_id": configs["twitter_client_id"],
    "redirect_uri":"http://127.0.0.1:5000/logged",
    "scope":"tweet.read users.read follows.read offline.access",
    "state":"state",
    "code_challenge":"challenge",
    "code_challenge_method":"plain"}

    authlink = url + urllib.parse.urlencode(parameters)
    
    

    return '<a href="{}">fuck</a>'.format(authlink)

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

    resp = make_response(redirect("/cookied"))
    resp.set_cookie("access_token", token["access_token"], max_age=token["expires_in"])
    resp.set_cookie("refresh_token", token["refresh_token"], max_age=60000*30)

    return resp

@bp.route("/googed", methods=['POST'])
def googed():
    print(request.form)

    return "eh"

@bp.route("/cookied")
def cookied():
    a = request.cookies.get("access_token")
    b = request.cookies.get("refresh_token")
    
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
        

    url = "https://api.twitter.com/2/tweets?ids=1594154971846823936,1594336348806082561"
    headers = {
        "Authorization" : "Bearer {}".format(a)
    }

    r = requests.get(url, headers=headers)

    return r.text

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
        print(r.text)

    if b is not None:
        
        dataToSend = {
            "client_id": configs["twitter_client_id"],
            "token":b,
            "token_type_hint": "refresh_token"
        }

        r = requests.post(url, headers=headers, data=dataToSend)
        print(r.text)

    resp = make_response(redirect("/"))
    resp.set_cookie("access_token", "", expires=0)
    resp.set_cookie("refresh_token", "", expires=0)

    return resp