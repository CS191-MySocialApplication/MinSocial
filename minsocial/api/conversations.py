
import tweepy
from abc import ABCMeta, abstractmethod

from mastodon import Mastodon

from minsocial import consts

import json

class Message(metaclass=ABCMeta):
    # TODO: Group conversation handling 
    def __init__(self, messageID, content, author, conversationID, createdTime):
        self.messageID = messageID
        self.content = content
        self.author = author
        self.conversationID = conversationID
        self.createdTime = createdTime

    def asdict(self):
        return {
            'source': self.source,
            'messageID': self.messageID,
            'content': self.content,
            'author': self.author,
            'conversationID': self.conversationID,
            'createdTime': self.createdTime,
        }


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

    def __init__(self, conversationID, message):
        super().__init__(message["id"], message["content"], message["account"], conversationID, message["created_at"])


class ConversationList:
    def __init__(self, twtAccessKey=None, mstdnAccessKey=None):
        assert(twtAccessKey is not None or mstdnAccessKey is not None)

        self.conversationList:list[Message] = []
        self.errors:list[str] = []

        if twtAccessKey:
            self._twtGenerateConvList(twtAccessKey)

        if mstdnAccessKey:
            self._mstdnGenerateConvList(mstdnAccessKey)

        # self._sortMessagesByTime()


    def _twtGenerateConvList(self, twtAccessKey):
        client = tweepy.Client(twtAccessKey, return_type=dict)

        direct_messages = client.get_direct_message_events( dm_event_fields=["id", "text", "dm_conversation_id", "sender_id", "created_at"], 
                                                            event_types="MessageCreate",
                                                            expansions=["sender_id"], 
                                                            user_fields=["username"], 
                                                            user_auth=False)

        if "includes" in direct_messages:

            users = {user["id"]: user for user in direct_messages["includes"]["users"]}

            convs = {}

            for messages in direct_messages["data"]:
                convs.setdefault(messages["dm_conversation_id"], 
                                TwtMsg(messages, users[messages["sender_id"]]).asdict())

            self.conversationList.extend(convs.values())


    def _mstdnGenerateConvList(self, mstdnAccessKey):
        client = Mastodon(api_base_url=consts.MSTDN_API_BASE_URL, access_token=mstdnAccessKey)

        conversations = client.conversations()

        self.conversationList.extend([MstdnMsg(conv["id"], conv["last_status"]).asdict() for conv in conversations])


    def _sortMessagesByTime(self):
        self.conversationList.sort(key=lambda x: x.createdTime, reverse=True)


class TwtConversation:

    def __init__(self, twtAccessKey, convID):
        
        self.messagesList = []

        self._twtGenerateConv(twtAccessKey, convID)
        

    def _twtGenerateConv(self, twtAccessKey, convID):
        client = tweepy.Client(twtAccessKey, return_type=dict)
        convs = client.get_direct_message_events(dm_conversation_id=convID, user_auth=False)

        self.messagesList.extend(convs["data"])


class MstdnConversation:

    def __init__(self, mstdnAccessKey, messageID):

        self.messagesList = []

        self._mtsdnGenerateConv(mstdnAccessKey, messageID)

    
    def _mtsdnGenerateConv(self, mstdnAccessKey, messageID):
        # TODO: Convert messages in mastodon to a uniform type
        client = Mastodon(api_base_url=consts.MSTDN_API_BASE_URL, access_token=mstdnAccessKey)
        response = client.status_context(messageID) 

        self.messagesList.extend(response["ancestors"])