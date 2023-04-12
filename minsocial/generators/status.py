from mastodon import Mastodon

from minsocial.models.status import Toot

from minsocial import consts


def generate_mstdn_status(status_id, mstdn_access_key):

    client = Mastodon(api_base_url=consts.MSTDN_API_BASE_URL, access_token=mstdn_access_key)

    toot = client.status(status_id)

    return Toot(toot).asdict()
