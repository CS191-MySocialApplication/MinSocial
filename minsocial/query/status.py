from abc import ABCMeta, abstractmethod
from enum import Enum

import tweepy
from tweepy import Response

from mastodon import Mastodon

from datetime import datetime, timezone

class Status(metaclass=ABCMeta):

    def __init__(self, statusID, author, createdTime, content):

        self.id = statusID
        self.author = author # TODO: Is there anyway to standardize this
        self.createdTime = createdTime
        self.content = content

    def asdict(self):
        return {
            'source': self.source,
            'id': self.id,
            'author': self.author,
            'createdTime': self.createdTime.isoformat(),
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
        createdTime = createdTime.replace(tzinfo=timezone.utc)

        super().__init__(toot["id"], toot["account"], createdTime, toot["content"])


class Timeline:

    def __init__(self, twtAccessKey = None, mstdnAccessKey = None):

        assert(twtAccessKey is not None or mstdnAccessKey is not None)

        self.statusList:list[Status] = []
        self.dictStatusList:list[dict] = []
        self.accessed = []
        self.errors:list[str] = []

        if twtAccessKey:
            self._twtGenerateTimeline(twtAccessKey)
            self.accessed.append("Twitter")

        if mstdnAccessKey:
            self._mstdnGenerateTimeline(mstdnAccessKey)
            self.accessed.append("Mastodon")

        self._sortStatusesByTime()


    def _twtGenerateTimeline(self, twtAccessKey):
        
        client = tweepy.Client(twtAccessKey, return_type=dict)
        user = client.get_me(user_auth=False)
        
        assert("id" in user["data"])
        
        response = client.get_users_mentions(user["data"]["id"], user_auth=False, expansions=["author_id"], tweet_fields=["id", "text", "created_at"])

        assert("users" in response["includes"])

        authors = dict()

        # TODO: Refactor this
        for author in response["includes"]["users"]:
            authors[author["id"]] = author

        for tweet in response["data"]:
            tweet = Tweet(tweet, authors[tweet["author_id"]])
            self.statusList.append(tweet)
            self.dictStatusList.append(tweet.asdict())


    def _mstdnGenerateTimeline(self, mstdnAccessKey):
        
        client = Mastodon(api_base_url="https://social.up.edu.ph", access_token=mstdnAccessKey)
        response = client.notifications(mentions_only=True)
        
        for notif in response:
            toot = Toot(notif["status"])
            self.statusList.append(toot)
            self.dictStatusList.append(toot.asdict())


    def _sortStatusesByTime(self):
        self.statusList.sort(key=lambda x: x.createdTime, reverse=True)


    def asdict(self):
        return self.dictStatusList


    def response(self):
        return {
            "data": self.dictStatusList,
            "accessed": self.accessed
        }


    def __getitem__(self, index):
        return self.statusList[index]
    

    def __iter__(self):
        yield from self.statusList