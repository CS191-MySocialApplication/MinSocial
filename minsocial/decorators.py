from flask import (
    redirect, url_for, request, make_response
)

from functools import wraps
import requests
import json

with open("config.json", "r", encoding="utf-8") as config_file:
        configs = json.loads(config_file.read())

def twt_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "refresh_token" not in request.cookies:
            return redirect(url_for("twtauth.log_in"))
        
        if "twt_access_token" not in request.cookies:

            url = "https://api.twitter.com/2/oauth2/token"
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            
            dataToSend = {
                "refresh_token": request.cookies.get("refresh_token"),
                "grant_type":"refresh_token",
                "client_id": configs["twitter_client_id"],
            }

            r = requests.post(url, headers=headers, data=dataToSend)
            token = r.json()

            response = redirect(request.url)
            response = make_response(response)

            response.set_cookie("access_token", token["access_token"], max_age=3600)

            return response

        return f(*args, **kwargs)

    return decorated_function        
        