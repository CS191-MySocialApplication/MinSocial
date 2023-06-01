from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
from minsocial.generators.replies import generate_replies_timeline


replies_bp = Blueprint('replies', __name__, url_prefix='/replies')

@replies_bp.route("/")
@authenticate
@wrap_json
def home():

    # Returns a list of Statuses that reply to the current user.

    twt_access_key = request.cookies.get("twtAccessToken")
    mstdn_access_key = request.cookies.get("mstdnAccessToken")

    timeline = generate_replies_timeline(twt_access_key=twt_access_key, mstdn_access_key=mstdn_access_key)

    return timeline