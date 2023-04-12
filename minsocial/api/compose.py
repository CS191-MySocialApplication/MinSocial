from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
from minsocial import consts

import tweepy
from mastodon import Mastodon

compose_bp = Blueprint('compose', __name__, url_prefix='/compose')


@compose_bp.route("/", methods=['POST'])
@authenticate
@wrap_json
def compose_tweet():
    if request.form["text"] == None:
        return {"status": "failed"}

    twtAccess = request.cookies.get("twtAccessToken")
    mstdnAccess = request.cookies.get("mstdnAccessToken")

    # if twtAccess:
    #     client = tweepy.Client(twtAccess, return_type=dict)
    #     twtdata = client.create_tweet(text=request.form['text'], user_auth=False)
    

    if mstdnAccess:
        client = Mastodon(api_base_url=consts.MSTDN_API_BASE_URL, access_token=mstdnAccess)
        toot = client.status_post(request.form['text'])


    return {"status": "success"}