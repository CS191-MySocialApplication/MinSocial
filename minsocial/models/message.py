from abc import ABCMeta, abstractmethod
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

class Message(metaclass=ABCMeta):
    # TODO: Group conversation handling 
    def __init__(self, messageID, unread, content, author, conversationID, createdTime, participantIDs, statusDict):
        
        self.messageID = messageID
        self.unread = unread
        self.content = content
        self.author = author
        self.conversationID = conversationID
        self.createdTime = createdTime
        self.participantIDs = participantIDs
        self.statusDict = statusDict


    def asdict(self):
        return {
            'messageID': self.messageID,
            'unread': self.unread,
            'content': self.content,
            'author': self.author,
            'conversationID': self.conversationID,
            'createdTime': self.createdTime,
            'participantIDs': self.participantIDs,
            'statusDict': self.statusDict,
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

    def __init__(self, conversationID, unread, message, participantIDs, statusDict):
        message["created_at"] = message["created_at"].astimezone(ZoneInfo("Asia/Manila"))
        message["created_at"] = message["created_at"].strftime("%d %b %y %H:%M")
        super().__init__(str(message["id"]), unread, message["content"], message["account"], str(conversationID), message["created_at"], list(participantIDs), statusDict)