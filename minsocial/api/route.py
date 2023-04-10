from flask import (
    Blueprint, redirect, render_template, request, url_for, send_from_directory, jsonify
)

from minsocial.decorators import wrap_json, authenticate
from minsocial.query.status import Timeline, MstdnContext
from minsocial.query.conversations import ConversationList, MstdnConversation, TwtConversation

import tweepy
from mastodon import Mastodon

bp = Blueprint('api', __name__, url_prefix='/api/')


@bp.route("/home")
@authenticate
@wrap_json
def home():

    twtAccess = request.cookies.get("twtAccessToken")
    mstdnAccess = request.cookies.get("mstdnAccessToken")

    timeline = Timeline(twtAccessKey=twtAccess, mstdnAccessKey=mstdnAccess)

    return timeline.response()


@bp.route("/messages")
@authenticate
@wrap_json
def messages():

    twtAccess = request.cookies.get("twtAccessToken")
    mstdnAccess = request.cookies.get("mstdnAccessToken")

    conversations = ConversationList(twtAccessKey=twtAccess, mstdnAccessKey=mstdnAccess)

    return conversations.conversationList


@bp.route("/messages/twt/<conversation_id>")
@authenticate
@wrap_json
def twtconversation(conversation_id):
    twtAccess = request.cookies.get("twtAccessToken")
    
    messageList = TwtConversation(twtAccess, conversation_id)

    return messageList.messagesList


@bp.route("/messages/mstdn/<conversation_id>")
@authenticate
@wrap_json
def mstdnconversation(conversation_id):
    mstdnAccess = request.cookies.get("mstdnAccessToken")
    
    messageList = MstdnConversation(mstdnAccess, conversation_id)


    return messageList.messagesList


@bp.route("/tweet/<tweet_id>")
@authenticate
@wrap_json
def view_tweet(tweet_id): # TODO: ADD MORE DETAILS
    a = request.cookies.get("twtAccessToken")

    client = tweepy.Client(a)

    tweet = client.get_tweet(   tweet_id, 
                                expansions=["referenced_tweets.id", "in_reply_to_user_id"],
                                tweet_fields=["conversation_id", "author_id", "in_reply_to_user_id", "referenced_tweets"],
                                user_fields=["id", "username"])

    return dict(tweet.data)


@bp.route("/toot/<toot_id>")
@authenticate
@wrap_json
def view_toot(toot_id): 
    a = request.cookies.get("mstdnAccessToken")
    client = Mastodon(api_base_url="https://social.up.edu.ph", access_token=a)

    toot = client.status(toot_id)

    return toot


@bp.route("/context/toot/<toot_id>")
@authenticate
@wrap_json
def view_toot_context(toot_id):
    a = request.cookies.get("mstdnAccessToken")

    context = MstdnContext(toot_id, a)

    return context.context


@bp.route("/compose", methods=['GET', 'POST'])
@authenticate
@wrap_json
def compose_tweet():
    if request.method == "GET":
        return "Hello"

    if request.form["text"] == None:
        return "hello"

    twtAccess = request.cookies.get("twtAccessToken")
    mstdnAccess = request.cookies.get("mstdnAccessToken")

    if twtAccess:
        client = tweepy.Client(twtAccess, return_type=dict)
        twtdata = client.create_tweet(text=request.form['text'], user_auth=False)
    

    if mstdnAccess:
        client = Mastodon(api_base_url="https://social.up.edu.ph", access_token=mstdnAccess)
        toot = client.status_post(request.form['text'])


    return {"status": "success"}


