from mastodon import Mastodon
from minsocial.models.status import Toot


def generate_mentions_timeline(twt_access_key=None, mstdn_access_key=None):
    assert(twt_access_key or mstdn_access_key)

    mentions_timeline = []

    if twt_access_key:

        twt_mentions = generate_twt_mentions(twt_access_key)
        mentions_timeline.extend(twt_mentions)

    if mstdn_access_key:

        mstdn_mentions = generate_mstdn_mentions(mstdn_access_key)
        mentions_timeline.extend(mstdn_mentions)

    return mentions_timeline


def generate_twt_mentions(twt_access_key): # ISSUE: Twitter API will eventually be unaccessible

    pass


def generate_mstdn_mentions(mstdn_access_key):
    
    client = Mastodon(api_base_url="https://social.up.edu.ph", access_token=mstdn_access_key)
    response = client.notifications(mentions_only=True)
    
    for notif in response:
        yield Toot(notif["status"])
