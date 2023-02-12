from flask import (
    redirect, url_for, request, make_response
)

from functools import wraps
import requests
import json

from minsocial.userAuth.authHandler import TwtAuthHandler

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        twtRefresh = request.cookies.get("twtRefreshToken")
        twtAccess = request.cookies.get("twtAccessToken")

        mstdnAccess = request.cookies.get("mstdnAccessToken")

        if twtRefresh == None and mstdnAccess == None:
            return redirect(url_for("twtauth.log_in"))
        
        if twtRefresh and twtAccess == None:

            handler = TwtAuthHandler()

            token = handler.refresh_access_token(twtRefresh)

            response = redirect(request.url)
            response = make_response(response)

            response.set_cookie("twtAccessToken", token["access_token"], max_age=3600)

            return response

        return f(*args, **kwargs)

    return decorated_function        
        