from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
from minsocial.generators.context import generate_mstdn_context

context_bp = Blueprint('context', __name__, url_prefix='/')


@context_bp.route("/context/toot/<toot_id>")
@authenticate
@wrap_json
def view_toot_context(toot_id):
    mstdn_access_key = request.cookies.get("mstdnAccessToken")

    context = generate_mstdn_context(toot_id, mstdn_access_key)

    return context