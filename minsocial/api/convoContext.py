from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
from minsocial.generators.convoContext import generate_mstdn_context

convoContext_bp = Blueprint('convoContext', __name__, url_prefix='/')


@convoContext_bp.route("/context/toot/<convo_id>/<toot_id>")
@authenticate
@wrap_json
def view_toot_context(toot_id, convo_id):
    mstdn_access_key = request.cookies.get("mstdnAccessToken")

    context = generate_mstdn_context(toot_id, mstdn_access_key, convo_id)

    return context