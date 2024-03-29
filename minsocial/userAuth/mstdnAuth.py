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
    
    handler = MstdnAuthHandler(code)
    token = handler.get_tokens()

    resp = make_response(jsonify({"status": "success"}))
    resp.set_cookie("mstdnAccessToken", token["access_token"], max_age=3600, samesite="lax")

    return resp


@bp.route("/logout")
def logout():
    a = request.cookies.get("mstdnAccessToken")

    handler = MstdnAuthHandler()
    handler.revoke_tokens(a)

    resp = make_response(jsonify({}))
    resp.set_cookie("mstdnAccessToken", "", expires=0, samesite="lax")

    return resp, 200