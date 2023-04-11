from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
from minsocial.generators.timeline import generate_mentions_timeline


mentions_bp = Blueprint('mentions', __name__, url_prefix='/mentions')

@bp.route("/home")
@authenticate
@wrap_json
def home():

    # Returns a list of Statuses that mentions the current user.

    twtAccess = request.cookies.get("twtAccessToken")
    mstdnAccess = request.cookies.get("mstdnAccessToken")

    timeline = generate_mentions_timeline(twtAccessKey=twtAccess, mstdnAccessKey=mstdnAccess)

    return timeline