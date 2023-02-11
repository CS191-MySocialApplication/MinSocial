from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from minsocial.decorators import twt_login_required

import tweepy

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route("/home")
@twt_login_required
def home():

    a = request.cookies.get("access_token")
    client = tweepy.Client(a)

    user = client.get_me(user_auth=False)

    mentions = client.get_users_mentions(user.data.id, user_auth=False, expansions=["author_id"])

    return {"data": mentions.data[0].data, "authors":[ x.data for x in mentions.includes["users"]]}

    # return render_template("index.html", mentions=mentions.data)

@bp.route("/dm")
@twt_login_required
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

    return render_template("dms.html", dms=direct_messages.data, users=users)


@bp.route("/tweet/<tweet_id>")
@twt_login_required
def view_tweet(tweet_id): # TODO: ADD MORE DETAILS
    a = request.cookies.get("access_token")

    client = tweepy.Client(a)

    tweet = client.get_tweet(   tweet_id, 
                                expansions=["referenced_tweets.id", "in_reply_to_user_id"],
                                tweet_fields=["conversation_id", "author_id", "in_reply_to_user_id", "referenced_tweets"],
                                user_fields=["id", "username"])

    return tweet.data.text

@bp.route("/compose", methods=['GET', 'POST'])
@twt_login_required
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