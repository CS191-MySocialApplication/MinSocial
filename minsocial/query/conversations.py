
import tweepy
from abc import ABCMeta, abstractmethod

from mastodon import Mastodon

import json

class Message:
    # TODO: Group conversation handling 
    def __init__(self, messageID, content, author, conversationID, createdTime):
        self.messageID = messageID
        self.content = content
        self.author = author
        self.conversationID = conversationID
        self.createdTime = createdTime

    @property
    @abstractmethod
    def source(self):
        pass


    

class TwtMsg(Message):
    source = "Twitter"

    def __init__(self, message, user):

        super().__init__(message["id"], message["text"], user, message["dm_conversation_id"], message["created_at"])


class MstdnMsg(Message):
    source = "Mastodon"

    def __init__(self, id, message):
        super().__init__(message["id"], message["content"], message["account"], id, message["created_at"])


class ConversationList:
    def __init__(self, twtAccessKey=None, mstdnAccessKey=None):
        assert(twtAccessKey is not None or mstdnAccessKey is not None)

        self.conversationList:list[Message] = []
        self.errors:list[str] = []

        if twtAccessKey:
            self._twtGenerateConversation(twtAccessKey)

        if mstdnAccessKey:
            self._mstdnGenerateConversation(mstdnAccessKey)


    def _twtGenerateConversation(self, twtAccessKey):
        client = tweepy.Client(twtAccessKey, return_type=dict)

        direct_messages = client.get_direct_message_events( dm_event_fields=["id", "text", "dm_conversation_id", "sender_id", "created_at"], 
                                                            event_types="MessageCreate",
                                                            expansions=["sender_id"], 
                                                            user_fields=["username"], 
                                                            user_auth=False)

        users = {user["id"]: user for user in direct_messages["includes"]["users"]}

        convs = {}

        for messages in direct_messages["data"]:
            convs.setdefault(messages["dm_conversation_id"], 
                             TwtMsg(messages, users[messages["sender_id"]]))

        self.conversationList.extend(convs.values())


    def _mstdnGenerateConversation(self, mstdnAccessKey):
        client = Mastodon(api_base_url="https://social.up.edu.ph", access_token=mstdnAccessKey)

        conversations = client.conversations()

        self.conversationList.extend([MstdnMsg(conv["id"], conv["last_status"]) for conv in conversations])

class Conversation:
    def __init__(self):
        pass

class MstdnConversation(Conversation):
    def __init__(self):
        pass

class TwtConversation(Conversation):
    def __init__(self):
        pass