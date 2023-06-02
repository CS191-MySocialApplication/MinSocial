from flask import (
    Blueprint, request
)

from minsocial.decorators import wrap_json, authenticate
from minsocial.generators.status import generate_mstdn_status

message_bp = Blueprint('message', __name__, url_prefix='/')


@message_bp.route("/msg/<toot_id>")
@authenticate
@wrap_json
def view_toot(toot_id): 

    # Return Toot with corresponding toot_id

    mstdn_access_key = request.cookies.get("mstdnAccessToken")
    
    toot = generate_mstdn_status(toot_id, mstdn_access_key)

    return toot
