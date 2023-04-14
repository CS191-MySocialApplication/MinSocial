from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
from minsocial.generators.conversation import generate_mstdn_conversation

conversation_bp = Blueprint('conversation', __name__, url_prefix='/')

@conversation_bp.route("/messages/mstdn/<conversation_id>")
@authenticate
@wrap_json
def mstdnconversation(conversation_id):

    # From a status id, return the conversation.

    mstdn_access_key = request.cookies.get("mstdnAccessToken")
    
    messageList = generate_mstdn_conversation(conversation_id, mstdn_access_key)

    return messageList