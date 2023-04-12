from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
from minsocial.generators.timeline import generate_mentions_timeline


mentions_bp = Blueprint('mentions', __name__, url_prefix='/home')

@mentions_bp.route("/")
@authenticate
@wrap_json
def home():

    # Returns a list of Statuses that mentions the current user.

    twtAccess = request.cookies.get("twtAccessToken")
    mstdn_access_key = request.cookies.get("mstdnAccessToken")

    timeline = generate_mentions_timeline(twtAccessKey=twtAccess, mstdn_access_key=mstdn_access_key)

    return timeline