from mastodon import Mastodon

from minsocial.models.status import Toot


def generate_mstdn_context(status_id, mstdn_access_key):

    client = Mastodon(api_base_url="https://social.up.edu.ph", access_token=mstdn_access_key)

    context = client.status_context(status_id)

    parents = []

    if "ancestors" in context:
        parents.extend([Toot(x).asdict() for x in context["ancestors"]])

    return parents
