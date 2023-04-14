from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
from minsocial.generators.conversation_list import generate_conversation_list

conversation_list_bp = Blueprint('messages', __name__, url_prefix='/')

@conversation_list_bp.route("/messages")
@authenticate
@wrap_json
def messages():

    # Returns a list of Conversations with the current user

    twt_access_key = request.cookies.get("twtAccessToken")
    mstdn_access_key = request.cookies.get("mstdnAccessToken")

    conversations = generate_conversation_list(twt_access_key=twt_access_key, mstdn_access_key=mstdn_access_key)

    return conversations