from flask import (
    Blueprint, redirect, render_template, request, url_for, send_from_directory, jsonify
)


bp = Blueprint('pages', __name__, url_prefix='/')

@bp.route("/")
def base():
    return send_from_directory('../client/dist', "index.html")


@bp.route("/logged")
def logged():
    return send_from_directory('../client/dist/callback', "index.html")


@bp.route("/home")
def home():
    return send_from_directory('../client/dist/home', "index.html")


@bp.route("/messages")
def message():
    return send_from_directory('../client/dist/messages', "index.html")


@bp.route("/<path:path>")
def sendfile(path):
    return send_from_directory('../client/dist', path)
