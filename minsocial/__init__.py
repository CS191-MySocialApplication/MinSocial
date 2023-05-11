from flask import Flask
from minsocial.api import api
from minsocial.userAuth import mstdnAuth, twtAuth
from minsocial.pages import routes

from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__, static_url_path="/static", static_folder='../client/build/static')

    app.register_blueprint(twtAuth.bp)
    app.register_blueprint(mstdnAuth.bp)
    app.register_blueprint(api.api_blueprint)
    app.register_blueprint(routes.bp)

    load_dotenv()

    assert os.getenv("mastodon_api_base_url")
    assert os.getenv("mastodon_client_id")
    assert os.getenv("mastodon_client_secret")
    assert os.getenv("server_host_url")

    return app