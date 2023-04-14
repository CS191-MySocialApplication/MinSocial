from abc import ABCMeta, abstractmethod


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
        super().__init__(str(message["id"]), message["content"], message["account"], str(conversationID), message["created_at"])