from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from minsocial.decorators import twt_login_required

from mastodon import Mastodon

bp = Blueprint('mstdn', __name__, url_prefix='/mstdn/')

@bp.route("/home") # @twt_login_required
def home():
    a = request.cookies.get("mstdn_access_token")
    client = Mastodon(api_base_url="https://social.up.edu.ph", access_token=a)
    posts = client.notifications(mentions_only=True)

    return render_template("mstdn_index.html", mentions=posts)

@bp.route("/dm")
def dm():
    a = request.cookies.get("mstdn_access_token")
    client = Mastodon(api_base_url="https://social.up.edu.ph", access_token=a)

    conversations = client.conversations()

    return render_template("mstdn_dms.html", conversations=conversations)


@bp.route("/status/<statusId>")
def viewStatus(statusId): # TODO: ADD MORE DETAILS
    a = request.cookies.get("mstdn_access_token")
    client = Mastodon(api_base_url="https://social.up.edu.ph", access_token=a)

    status = client.status(statusId)

    return status["content"]

@bp.route("/compose", methods=['GET', 'POST'])
def compose_tweet():
    if request.method == "GET":
        return redirect(url_for("mstdn.home"))

    if request.form["text"] == None:
        return redirect(url_for("mstdn.home"))

    a = request.cookies.get("access_token")
    client = Mastodon(api_base_url="https://social.up.edu.ph", access_token=a)

    toot = client.toot(request.form["text"])
    
    return redirect(url_for('mstdn.viewStatus', statusId=toot["id"]))
