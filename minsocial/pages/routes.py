from flask import (
    Blueprint, redirect, render_template, request, url_for, send_from_directory, jsonify
)


bp = Blueprint('pages', __name__, url_prefix='/')

@bp.route("/")
def base():
    return send_from_directory('../client/dist', "index.html")


@bp.route("/callback/twt")
def callbackTwt():
    return send_from_directory('../client/dist/callback/twt', "index.html")


@bp.route("/callback/mstdn")
def callbackMstdn():
    return send_from_directory('../client/dist/callback/mstdn', "index.html")


@bp.route("/home")
def home():
    return send_from_directory('../client/dist/home', "index.html")


@bp.route("/messages")
def message():
    return send_from_directory('../client/dist/messages', "index.html")

@bp.route("/replies")
def reply():
    return send_from_directory('../client/dist/replies', "index.html")

@bp.route("/indivMention")
def indivMention():
    return send_from_directory('../client/dist/indivMention', "index.html")

@bp.route("/<path:path>")
def sendfile(path):
    return send_from_directory('../client/dist', path)
