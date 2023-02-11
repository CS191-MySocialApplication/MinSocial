from abc import ABCMeta, abstractmethod
from enum import Enum

import tweepy
from tweepy import Response

from mastodon import Mastodon

class Status(metaclass=ABCMeta):

    def __init__(self, statusID, author, createdTime, content):

        self.id = statusID
        self.author = author
        self.created_time = createdTime
        self.content = content

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

        super().__init__(data["id"], author, data["created_at"], data["text"])


class Toot(Status):
    source = "Mastodon"

    def __init__(self, toot: dict[str, any]):
        
        assert("id" in toot)
        assert("account" in toot)
        assert("created_at" in toot)
        assert("content" in toot)

        super().__init__(toot["id"], toot["account"], toot["created_at"], toot["content"])


class Timeline:

    def __init__(self, twtAccessKey = None, mstdnAccessKey = None):

        assert(twtAccessKey is not None or mstdnAccessKey is not None)

        self.statusList:list[Status] = []
        self.errors:list[str] = []

        if twtAccessKey:
            self._twtGenerateTimeline(twtAccessKey)

        if mstdnAccessKey:
            self._mstdnGenerateTimeline(mstdnAccessKey)

        self._sortStatusesByTime()


    def _twtGenerateTimeline(self, twtAccessKey):
        
        client = tweepy.Client(twtAccessKey)
        user = client.get_me(user_auth=False)
        
        assert("id" in user.data)
        
        response = client.get_users_mentions(user.data["id"], user_auth=False, expansions=["author_id"])

        assert("users" in response.includes)

        authors = dict()

        for author in response.includes["users"]:
            authors[author["id"]] = author

        for tweet in response.data:
            self.statusList.append(Tweet(tweet, authors[tweet["author_id"]]))


    def _mstdnGenerateTimeline(self, mstdnAccessKey):
        pass
        

    def _sortStatusesByTime():
        pass


    def _processTweets():
        pass


    def __iter__():
        pass