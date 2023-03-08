from flask import (
    Blueprint, redirect, render_template, request, url_for, send_from_directory, jsonify
)


bp = Blueprint('pages', __name__, url_prefix='/')

@bp.route("/")
def base():
    return send_from_directory('../client/build', "index.html")

@bp.route("/logged")
def logged():
    return send_from_directory('../client/build', "logged.html")


@bp.route("/home")
def home():
    return send_from_directory('../client/build', "home.html")


@bp.route("/<path:path>")
def sendfile(path):
    print(path)
    return send_from_directory('../client/build', path)
