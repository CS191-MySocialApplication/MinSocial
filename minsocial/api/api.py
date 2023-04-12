from flask import Blueprint

from minsocial.api.conversation import conversation_bp
from minsocial.api.conversations_list import conversation_list_bp
from minsocial.api.mentions_timeline import mentions_bp


api_blueprint = Blueprint("api", __name__, url_prefix="/api/v2")

api_blueprint.register_blueprint(conversation_bp)
api_blueprint.register_blueprint(conversation_list_bp)
api_blueprint.register_blueprint(mentions_bp)
