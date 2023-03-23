from flask import (
    make_response, redirect, render_template, request, Blueprint, url_for, jsonify
)

import requests
import urllib.parse
import json

from minsocial.userAuth.authHandler import MstdnAuthHandler

bp = Blueprint('mstdnauth', __name__, url_prefix='/auth/mstdn')

@bp.route("/")
def log_in():
    
    handler = MstdnAuthHandler()

    return jsonify({"auth_url":handler.get_auth_url()})


@bp.route("/callback", methods=['GET'])
def callback():
    code = request.args["code"]
    
    print(code)

    handler = MstdnAuthHandler(code)
    token = handler.get_tokens()

    resp = make_response(jsonify({"status": "success"}))
    resp.set_cookie("mstdnAccessToken", token["access_token"], max_age=3600)

    return resp


@bp.route("/logout")
def logout():
    a = request.cookies.get("mstdnAccessToken")

    handler = MstdnAuthHandler()
    handler.revoke_tokens(a)

    resp = make_response(redirect("/"))
    resp.set_cookie("mstdnAccessToken", "", expires=0)

    return resp