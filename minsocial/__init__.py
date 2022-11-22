from flask import Flask
import json
from minsocial import auth

def create_app():
    app = Flask(__name__)
    
    

    app.register_blueprint(auth.bp)

    return app