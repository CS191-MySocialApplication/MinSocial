from flask import Blueprint

from minsocial.api.mentions_timeline import mentions_bp
from minsocial.api.conversation import conversation_bp
from minsocial.api.conversations_list import conversation_list_bp
from minsocial.api.statusv2 import status_bp
from minsocial.api.context import context_bp
from minsocial.api.compose import compose_bp
from minsocial.api.replies_timeline import replies_bp
from minsocial.api.message import message_bp
from minsocial.api.composeMsg import composeMsg_bp
from minsocial.api.composeMsgv2 import composeMsgv2_bp
from minsocial.api.poll import poll_bp
from minsocial.api.convoContext import convoContext_bp


api_blueprint = Blueprint("apiv2", __name__, url_prefix="/api")

api_blueprint.register_blueprint(conversation_bp)
api_blueprint.register_blueprint(conversation_list_bp)
api_blueprint.register_blueprint(mentions_bp)
api_blueprint.register_blueprint(status_bp)
api_blueprint.register_blueprint(context_bp)
api_blueprint.register_blueprint(compose_bp)
api_blueprint.register_blueprint(poll_bp)
api_blueprint.register_blueprint(replies_bp)
api_blueprint.register_blueprint(message_bp)
api_blueprint.register_blueprint(composeMsg_bp)
api_blueprint.register_blueprint(composeMsgv2_bp)
api_blueprint.register_blueprint(convoContext_bp)