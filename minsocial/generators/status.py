from mastodon import Mastodon

from minsocial.models.status import Toot

import os


def generate_mstdn_status(status_id, mstdn_access_key):

    client = Mastodon(api_base_url=os.getenv("mastodon_api_base_url"), access_token=mstdn_access_key)

    toot = client.status(status_id)
    toot["id"] = str(toot["id"])

    return toot
