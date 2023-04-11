
from mastodon import Mastodon

from minsocial import consts

def generate_mstdn_conversation(message_id, mstdn_access_key):

    # Returns the parents of a message
    # TODO: Make data model for messages (still Mastodon statuses)

    client = client = Mastodon(api_base_url=consts.MSTDN_API_BASE_URL, access_token=mstdn_access_key)
    response = client.status_context(message_id) 

    return response["ancestors"]