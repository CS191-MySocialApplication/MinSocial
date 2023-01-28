from flask import request
from flask import make_response
from flask import render_template
from flask import redirect
from datetime import datetime, timedelta
import requests
import urllib.parse
import json
from minsocial.decorators import login_required
from minsocial import constants

import tweepy

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route("/home")
@login_required
def home():

    a = request.cookies.get("access_token")
    user_id = request.cookies.get("id")

    client = tweepy.Client(a)
    mentions = client.get_users_mentions(user_id)

    return render_template("index.html", mentions=mentions.data)

@bp.route("/dm")
@login_required
def dm():
    a = request.cookies.get("access_token")

    client = tweepy.Client(a)
    direct_messages = client.get_direct_message_events( dm_event_fields=["id", "text", "dm_conversation_id", "sender_id"], 
                                                        expansions=["sender_id"], 
                                                        user_fields=["username"], 
                                                        user_auth=False)
        
    users = {}
    for user in direct_messages.includes["users"]:
        users[user.id] = user.username

    print(users)

    return render_template("dms.html", dms=direct_messages.data, users=users)


@bp.route("/tweet/<tweet_id>")
@login_required
def view_tweet(tweet_id): # TODO: ADD MORE DETAILS
    a = request.cookies.get("access_token")

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