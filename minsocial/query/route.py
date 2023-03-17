from flask import (
    Blueprint, redirect, render_template, request, url_for, send_from_directory, jsonify
)

from minsocial.decorators import login_required
from minsocial.query.status import Timeline
from minsocial.query.conversations import ConversationList, MstdnConversation, TwtConversation

import tweepy
from mastodon import Mastodon

bp = Blueprint('api', __name__, url_prefix='/api/')


@bp.route("/home")
@login_required
def home():

    twtAccess = request.cookies.get("twtAccessToken")
    mstdnAccess = request.cookies.get("mstdnAccessToken")

    timeline = Timeline(twtAccessKey=twtAccess, mstdnAccessKey=mstdnAccess)

    return jsonify(timeline.asdict())


@bp.route("/messages")
@login_required
def messages():

    twtAccess = request.cookies.get("twtAccessToken")
    mstdnAccess = request.cookies.get("mstdnAccessToken")

    client = tweepy.Client(twtAccess, return_type=dict)

    TWTdms = client.get_direct_message_events( dm_event_fields=["id", "text", "dm_conversation_id", "sender_id", "created_at"], 
                                                            event_types="MessageCreate",
                                                            expansions=["sender_id"], 
                                                            user_fields=["username"], 
                                                            user_auth=False)

    dictTWTDMs = dict(TWTdms) # Do this for Mastodon when it's implemented
    for dm in dictTWTDMs["data"]:
        dm.__setitem__('source', 'Twitter')

    return jsonify(dictTWTDMs)


@bp.route("/messages/twt/<conversation_id>")
@login_required
def twtconversation(conversation_id):
    twtAccess = request.cookies.get("twtAccessToken")
    
    messageList = TwtConversation(twtAccess, conversation_id)

    return messageList.messagesList


@bp.route("/messages/mstdn/<conversation_id>")
@login_required
def mstdnconversation(conversation_id):
    mstdnAccess = request.cookies.get("mstdnAccessToken")
    
    messageList = MstdnConversation(mstdnAccess, conversation_id)


    return messageList.messagesList


@bp.route("/tweet/<tweet_id>")
@login_required
def view_tweet(tweet_id): # TODO: ADD MORE DETAILS
    a = request.cookies.get("twtAccessToken")

    client = tweepy.Client(a)

    tweet = client.get_tweet(   tweet_id, 
                                expansions=["referenced_tweets.id", "in_reply_to_user_id"],
                                tweet_fields=["conversation_id", "author_id", "in_reply_to_user_id", "referenced_tweets"],
                                user_fields=["id", "username"])

    return jsonify(dict(tweet.data))


@bp.route("/toot/<toot_id>")
def view_toot(toot_id): 
    a = request.cookies.get("mstdnAccessToken")
    client = Mastodon(api_base_url="https://social.up.edu.ph", access_token=a)

    toot = client.status(toot_id)

    return toot


@bp.route("/compose", methods=['GET', 'POST'])
@login_required
def compose_tweet():
    if request.method == "GET":
        return "Hello"

    if request.form["text"] == None:
        return "hello"

    a = request.cookies.get("twtAccessToken")
    client = tweepy.Client(a)

    tweet = client.create_tweet(text=request.form['text'], user_auth=False)
    
    if len(tweet.errors) == 0:
        data = tweet.data
        return "Good"

    return "hello"


