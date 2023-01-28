from flask import Flask
from minsocial import auth, queries

def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth.bp)
    app.register_blueprint(queries.bp)

    return app