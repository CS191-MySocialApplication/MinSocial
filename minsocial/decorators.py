from flask import (
    redirect, url_for, request, make_response, jsonify
)

from functools import wraps
import requests
import json

from minsocial.userAuth.authHandler import TwtAuthHandler

def wrap_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return jsonify(f(*args, **kwargs))

    return decorated_function

def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        # 200 - Both are returned
        # 206 - Only Mastodon or Twitter
        # 403 - No Auth

        twtRefresh = request.cookies.get("twtRefreshToken")
        twtAccess = request.cookies.get("twtAccessToken")

        mstdnAccess = request.cookies.get("mstdnAccessToken")

        if twtRefresh == None and mstdnAccess == None:
            return jsonify({}), 403
        
        if twtAccess == None or mstdnAccess == None:
            return f(*args, **kwargs), 206

        return f(*args, **kwargs), 200

    return decorated_function        
        