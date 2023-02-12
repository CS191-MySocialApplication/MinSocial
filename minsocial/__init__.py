from flask import Flask
from minsocial.query import mstdnqueries
from minsocial.query import route
from minsocial.userAuth import mstdnauth, twtauth

def create_app():
    app = Flask(__name__)

    app.register_blueprint(twtauth.bp)
    app.register_blueprint(mstdnauth.bp)
    app.register_blueprint(route.bp)
    app.register_blueprint(mstdnqueries.bp)

    return app