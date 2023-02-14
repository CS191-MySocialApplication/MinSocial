from flask import Flask
from minsocial.query import mstdnqueries
from minsocial.query import route
from minsocial.userAuth import mstdnAuth, twtAuth

def create_app():
    app = Flask(__name__)

    app.register_blueprint(twtAuth.bp)
    app.register_blueprint(mstdnAuth.bp)
    app.register_blueprint(route.bp)
    app.register_blueprint(mstdnqueries.bp)

    return app