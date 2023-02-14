from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from minsocial.decorators import login_required
from minsocial.query.status import Timeline

import tweepy

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route("/home")
@login_required
def home():

    twtAccess = request.cookies.get("twtAccessToken")
    mstdnAccess = request.cookies.get("mstdnAccessToken")

    timeline = Timeline(twtAccessKey=twtAccess, mstdnAccessKey=mstdnAccess)

    return render_template("index.html", mentions=timeline)

@bp.route("/messages")
@login_required
def messages():
    a = request.cookies.get("twtAccessToken")

    client = tweepy.Client(a, return_type=dict)
    direct_messages = client.get_direct_message_events( dm_event_fields=["id", "text", "dm_conversation_id", "sender_id", "created_at"], 
                                                        event_types="MessageCreate",
                                                        expansions=["sender_id"], 
                                                        user_fields=["username"], 
                                                        user_auth=False)
        
    users = {}
    for user in direct_messages["includes"]["users"]:
        users[user["id"]] = user["username"]

    unique_conversations = {}

    for messages in direct_messages["data"]:
        if messages["dm_conversation_id"] not in unique_conversations:
            unique_conversations[messages["dm_conversation_id"]] = messages

    conversations = unique_conversations.values()

    return render_template("dms.html", dms=conversations, users=users)


@bp.route("/messages/<conversation_id>")
@login_required
def conversation(conversation_id):
    a = request.cookies.get("twtAccessToken")

    client = tweepy.Client(a, return_type=dict)
    
    conversationEvents = client.get_direct_message_events(dm_conversation_id=conversation_id,
                                                          user_auth=False)

    return conversationEvents


@bp.route("/tweet/<tweet_id>")
@login_required
def view_tweet(tweet_id): # TODO: ADD MORE DETAILS
    a = request.cookies.get("twtAccessToken")

    client = tweepy.Client(a)

    tweet = client.get_tweet(   tweet_id, 
                                expansions=["referenced_tweets.id", "in_reply_to_user_id"],
                                tweet_fields=["conversation_id", "author_id", "in_reply_to_user_id", "referenced_tweets"],
                                user_fields=["id", "username"])

    return tweet.data.text

@bp.route("/compose", methods=['GET', 'POST'])
@login_required
def compose_tweet():
    if request.method == "GET":
        return redirect(url_for("home.home"))

    if request.form["text"] == None:
        return redirect(url_for("home.home"))

    a = request.cookies.get("access_token")
    client = tweepy.Client(a)

    tweet = client.create_tweet(text=request.form['text'], user_auth=False)
    
    if len(tweet.errors) == 0:
        data = tweet.data
        return redirect(url_for('home.view_tweet', tweet_id=data["id"]))

    return redirect(url_for("home.home"))