from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
from minsocial.generators.conversation_list import generate_conversation_list

bp = Blueprint('messages', __name__, url_prefix='/messages')

@bp.route("/messages")
@authenticate
@wrap_json
def messages():

    # Returns a list of Conversations with the current user

    twtAccess = request.cookies.get("twtAccessToken")
    mstdnAccess = request.cookies.get("mstdnAccessToken")

    conversations = generate_conversation_list(twtAccessKey=twtAccess, mstdnAccessKey=mstdnAccess)

    return conversations