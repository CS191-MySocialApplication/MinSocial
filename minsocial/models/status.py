from abc import ABCMeta, abstractmethod
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

class Status(metaclass=ABCMeta):

    def __init__(self, statusID, author, createdTime, content):

        self.id = statusID
        self.author = author
        self.createdTime = createdTime
        self.content = content

    def asdict(self):
        return {
            'source': self.source,
            'id': self.id,
            'author': self.author,
            'createdTime': self.createdTime,
            'content': self.content
        }

    @property
    @abstractmethod
    def source(self):
        pass


class Tweet(Status):
    source = "Twitter"
    
    def __init__(self, data: dict[str, any], author: dict[str, any]):

        assert("id" in data)
        assert("author_id" in data)
        assert("created_at" in data)
        assert("text" in data) 

        createdTime = datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        createdTime = createdTime.replace(tzinfo=timezone.utc)

        super().__init__(data["id"], author, createdTime, data["text"])


class Toot(Status):
    source = "Mastodon"

    def __init__(self, toot: dict[str, any]):
        
        assert("id" in toot)
        assert("account" in toot)
        assert("created_at" in toot)
        assert("content" in toot)

        createdTime = toot["created_at"]
        createdTime = createdTime.astimezone(ZoneInfo("Asia/Manila"))
        createdTime = createdTime.strftime("%d %b %y %H:%M")

        super().__init__(str(toot["id"]), toot["account"], createdTime, toot["content"])