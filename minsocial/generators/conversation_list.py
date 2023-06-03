from mastodon import Mastodon

from minsocial.models.message import MstdnMsg

import os

def generate_conversation_list(twt_access_key=None, mstdn_access_key=None):
    assert(twt_access_key is not None or mstdn_access_key is not None)

    conversation_list = []

    if twt_access_key:
        twt_conversation_list = generate_twt_conversation_list(twt_access_key)
        conversation_list.extend(twt_conversation_list)

    if mstdn_access_key:
        mstdn_conversation_list = generate_mstdn_conversation_list(mstdn_access_key)
        conversation_list.extend(mstdn_conversation_list)

    return conversation_list


def generate_twt_conversation_list(twt_access_key): 

    # ISSUE: Twitter API will eventually be unaccessible

    pass


def generate_mstdn_conversation_list(mstdn_access_key):

    client = Mastodon(api_base_url=os.getenv("mastodon_api_base_url"), access_token=mstdn_access_key)

    conversations_list = client.conversations()

    for conversations in conversations_list:
        yield MstdnMsg(conversations["id"], conversations["unread"], conversations["last_status"], conversations["accounts"], client.status(conversations["last_status"]["id"])).asdict()