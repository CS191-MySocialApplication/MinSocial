from mastodon import Mastodon

from minsocial.models.status import Toot

from minsocial import consts


def generate_mstdn_context(status_id, mstdn_access_key):

    client = Mastodon(api_base_url=consts.MSTDN_API_BASE_URL, access_token=mstdn_access_key)

    context = client.status_context(status_id)

    parents = []

    if "ancestors" in context:
        parents.extend([Toot(x).asdict() for x in context["ancestors"]])

    return parents
