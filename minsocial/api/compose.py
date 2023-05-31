from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
import os

import json

import tweepy
from mastodon import Mastodon

compose_bp = Blueprint('compose', __name__, url_prefix='/compose')


@compose_bp.route("/", methods=['POST'])
@authenticate
@wrap_json
def compose_tweet(): 
    # TODO: Refactor code
    if request.form["text"] == None:
        return {"status": "failed"}
    
    mstdnAccess = request.cookies.get("mstdnAccessToken")
    
    if not mstdnAccess:
        return {"status": "failed"}

    client = Mastodon(api_base_url=os.getenv("mastodon_api_base_url"), access_token=mstdnAccess)

    attachmentType = request.form.get("attachmentType")

    if attachmentType == "media":
        media_ids = []
        for file in request.files.values():
            media = client.media_post(file, mime_type="image/png")
            media_ids.append(media["id"])

        toot = client.status_post(request.form['text'], media_ids=media_ids)
        
    elif attachmentType == "poll":
        option = request.form["option"] == "true"
        deadline = request.form["deadline"]
        choices = json.loads(request.form["choices"])

        poll = client.make_poll(choices, deadline, option)
        toot = client.status_post(request.form["text"], poll=poll)

    return {"status": "success"}