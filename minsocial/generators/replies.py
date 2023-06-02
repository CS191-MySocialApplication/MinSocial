from mastodon import Mastodon
from minsocial.models.status import Toot

import os
from zoneinfo import ZoneInfo
from datetime import datetime, timezone, timedelta

def generate_replies_timeline(twt_access_key=None, mstdn_access_key=None):
    assert(twt_access_key or mstdn_access_key)

    replies_timeline = []

    if twt_access_key:

        twt_replies = generate_twt_replies(twt_access_key)
        replies_timeline.extend(twt_replies)

    if mstdn_access_key:

        mstdn_replies = generate_mstdn_replies(mstdn_access_key)
        replies_timeline.extend(mstdn_replies)

    return replies_timeline


def generate_twt_replies(twt_access_key): # ISSUE: Twitter API will eventually be unaccessible

    pass


def generate_mstdn_replies(mstdn_access_key):
    
    client = Mastodon(api_base_url=os.getenv("mastodon_api_base_url"), access_token=mstdn_access_key)
    tl = []

    user = client.account_verify_credentials()
    
    response = client.notifications(mentions_only=True)

    for notif in response:
        if (len(client.status_context(notif["status"]["id"])["ancestors"]) and notif["status"]["visibility"]!='direct'):
            tl.append(notif["status"])

    sortTL = sorted(tl, key=lambda d: d['created_at'], reverse=True)

    for post in sortTL:
        post["id"] = str(post["id"])
        post["created_at"] = post["created_at"].astimezone(ZoneInfo("Asia/Manila"))
        post["created_at"] = post["created_at"].strftime("%d %b %y %H:%M")
        yield post
