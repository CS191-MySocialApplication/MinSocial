from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
import os

import json

import tweepy
from mastodon import Mastodon

poll_bp = Blueprint('poll', __name__, url_prefix='/poll')


@poll_bp.route("/", methods=['POST'])
@authenticate
@wrap_json
def view_poll(): 
    
    mstdnAccess = request.cookies.get("mstdnAccessToken")
    
    if not mstdnAccess:
        return {"status": "failed"}

    client = Mastodon(api_base_url=os.getenv("mastodon_api_base_url"), access_token=mstdnAccess)

    pollId = request.form["id"]

    new_poll = client.poll(pollId)
    return new_poll



@poll_bp.route("/vote", methods=['POST'])
@authenticate
@wrap_json
def vote_poll(): 
    
    mstdnAccess = request.cookies.get("mstdnAccessToken")
    
    if not mstdnAccess:
        return {"status": "failed"}

    client = Mastodon(api_base_url=os.getenv("mastodon_api_base_url"), access_token=mstdnAccess)

    pollId = request.form["id"]
    pollChoices = json.loads(request.form["choices"])
    client.poll_vote(pollId, pollChoices)
    newPoll = client.poll(pollId)

    return newPoll
