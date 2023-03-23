from flask import Flask
from minsocial.query import mstdnqueries
from minsocial.query import route
from minsocial.userAuth import mstdnAuth, twtAuth
from minsocial.pages import routes

def create_app():
    app = Flask(__name__, static_url_path="/static", static_folder='../client/build/static')

    app.register_blueprint(twtAuth.bp)
    app.register_blueprint(mstdnAuth.bp)
    app.register_blueprint(route.bp)
    # app.register_blueprint(mstdnqueries.bp)
    app.register_blueprint(routes.bp)

    return app