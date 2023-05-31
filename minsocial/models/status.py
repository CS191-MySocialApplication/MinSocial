from abc import ABCMeta, abstractmethod
from datetime import datetime, timezone


class Status(metaclass=ABCMeta):

    def __init__(self, statusID, author, createdTime, content, cw):

        self.id = statusID
        self.author = author
        self.createdTime = createdTime
        self.content = content
        self.cw = cw

    def asdict(self):
        return {
            'source': self.source,
            'id': self.id,
            'author': self.author,
            'createdTime': self.createdTime.isoformat(),
            'content': self.content,
            'cw': self.cw
        }

    @property
    @abstractmethod
    def source(self):
        pass


class Tweet(Status):
    source = "Twitter"
    
    def __init__(self, data, author):

        assert("id" in data)
        assert("author_id" in data)
        assert("created_at" in data)
        assert("text" in data) 

        createdTime = datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        createdTime = createdTime.replace(tzinfo=timezone.utc)

        super().__init__(data["id"], author, createdTime, data["text"])


class Toot(Status):
    source = "Mastodon"

    def __init__(self, toot):
        
        assert("id" in toot)
        assert("account" in toot)
        assert("created_at" in toot)
        assert("content" in toot)
        assert("spoiler_text" in toot)

        createdTime = toot["created_at"]
        createdTime = createdTime.replace(tzinfo=timezone.utc)

        super().__init__(str(toot["id"]), toot["account"], createdTime, toot["content"], toot["spoiler_text"])