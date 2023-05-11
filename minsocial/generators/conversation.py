
from mastodon import Mastodon

import os

def generate_mstdn_conversation(message_id, mstdn_access_key):

    # Returns the parents of a message
    # TODO: Make data model for messages (still Mastodon statuses)

    client = client = Mastodon(api_base_url=os.getenv("mastodon_api_base_url"), access_token=mstdn_access_key)
    response = client.status_context(message_id) 

    return response["ancestors"]