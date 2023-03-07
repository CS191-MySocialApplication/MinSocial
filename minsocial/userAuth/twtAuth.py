from flask import (
    make_response, redirect, render_template, request, Blueprint, jsonify
)

import requests
import urllib.parse
import json

from minsocial.userAuth.authHandler import TwtAuthHandler

bp = Blueprint('twtauth', __name__, url_prefix='/auth/twt')

@bp.route("/")
def log_in():
    
    handler = TwtAuthHandler()

    return jsonify({"auth_url":handler.get_auth_url()})

@bp.route("/logged", methods=['GET'])
def logged():
    code = request.args["code"]
    
    handler = TwtAuthHandler(code=code)
    token = handler.get_tokens()

    resp = make_response(redirect("/home"))
    resp.set_cookie("twtAccessToken", token["access_token"], max_age=3600)
    resp.set_cookie("twtRefreshToken", token["refresh_token"], max_age=3600)

    return resp

@bp.route("/logout")
def logout():
    a = request.cookies.get("twtAccessToken")
    b = request.cookies.get("twtRefreshToken")

    handler = TwtAuthHandler()
    handler.revoke_tokens(a, b)

    resp = make_response(redirect("/"))
    resp.set_cookie("twtAccessToken", "", expires=0)
    resp.set_cookie("twtRefreshToken", "", expires=0)

    return resp