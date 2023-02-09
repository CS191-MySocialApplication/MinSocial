from flask import Flask
from minsocial import queries, twtauth, mstdnauth, mstdnqueries

def create_app():
    app = Flask(__name__)

    app.register_blueprint(twtauth.bp)
    app.register_blueprint(mstdnauth.bp)
    app.register_blueprint(queries.bp)
    app.register_blueprint(mstdnqueries.bp)

    return app