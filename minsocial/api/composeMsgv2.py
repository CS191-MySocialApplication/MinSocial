from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
import os

import json

import tweepy
from mastodon import Mastodon

composeMsgv2_bp = Blueprint('composeMsgv2', __name__, url_prefix='/composeMsgv2')


@composeMsgv2_bp.route("/", methods=['POST'])
@authenticate
@wrap_json
def compose_newMsg(): 
    # TODO: Refactor code
    if request.form["text"] == None:
        return {"status": "failed"}
    
    mstdnAccess = request.cookies.get("mstdnAccessToken")
    
    if not mstdnAccess:
        return {"status": "failed"}

    client = Mastodon(api_base_url=os.getenv("mastodon_api_base_url"), access_token=mstdnAccess)

    sensitive = request.form["contentWarning"] == "true"
    spoiler_text = request.form["contentWarningText"] if sensitive else None

    attachmentType = request.form.get("attachmentType")

    media_ids = None
    poll = None

    if attachmentType == "media":
        media_ids = []
        for file in request.files.values():
            media = client.media_post(file, mime_type=file.mimetype)
            media_ids.append(media["id"])
        
    elif attachmentType == "poll":
        option = request.form["option"] == "true"
        deadline = request.form["deadline"]
        choices = json.loads(request.form["choices"])

        poll = client.make_poll(choices, deadline, option)
    
    toot = client.status_post(request.form["text"], 
                              media_ids=media_ids, 
                              poll=poll,
                              sensitive=sensitive,
                              spoiler_text=spoiler_text,
                              visibility='direct')

    return {"status": "success"}

