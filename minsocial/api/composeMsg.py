from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
import os

import json

import tweepy
from mastodon import Mastodon

composeMsg_bp = Blueprint('composeMsg', __name__, url_prefix='/composeMsg')


@composeMsg_bp.route("/", methods=['POST'])
@authenticate
@wrap_json
def compose_Msg(): 
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
    latestID = request.form["sendID"]

    media_ids = None
    poll = None

    if attachmentType == "media":
        media_ids = []
        for file in request.files.values():
            media = client.media_post(file, mime_type="image/png")
            media_ids.append(media["id"])
        
    elif attachmentType == "poll":
        option = request.form["option"] == "true"
        deadline = request.form["deadline"]
        choices = json.loads(request.form["choices"])

        poll = client.make_poll(choices, deadline, option)

    context = client.status_context(latestID)
    toot = client.status(latestID)

    toMention = client.me()['username']

    tootContext = context["ancestors"]+[toot]+context["descendants"]

    flag = False
    for toots in tootContext:
        if toots['account']['username']!=client.me()['username']:
            toMention = toots['account']['username']
            #print('user: ',toots['account']['username'],'\n')
            flag = True

        for mentioned in toots['mentions']:
            if mentioned['username']!=client.me()['username']:
                toMention = mentioned['username']
                #print('mentions: ',mentioned['username'],'\n')
                flag = True
                
        if flag == True:
            break
        
    print('Chosen: ',toMention)

    userMention = "@"+toMention+" "+request.form["text"]
    
    toot = client.status_post(userMention, 
                              media_ids=media_ids, 
                              poll=poll,
                              sensitive=sensitive,
                              spoiler_text=spoiler_text,
                              visibility='direct',
                              in_reply_to_id=str(latestID))
    

    return {"status": "success"}
