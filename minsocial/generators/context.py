from mastodon import Mastodon

from minsocial.models.status import Toot

import os
from zoneinfo import ZoneInfo
from datetime import datetime, timezone, timedelta

def generate_mstdn_context(status_id, mstdn_access_key):

    client = Mastodon(api_base_url=os.getenv("mastodon_api_base_url"), access_token=mstdn_access_key)

    context = client.status_context(status_id)
    toot = client.status(status_id)

    #tootContext = context["ancestors"]+[toot]+context["descendants"]
    tootContext = context["ancestors"]+[toot]
    print(tootContext)

    for posts in tootContext:
        posts["id"] = str(posts["id"])
        posts["created_at"] = posts["created_at"].astimezone(ZoneInfo("Asia/Manila"))
        posts["created_at"] = posts["created_at"].strftime("%d %b %y %H:%M")
        
    return tootContext
