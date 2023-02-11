from minsocial.status import (
    Timeline, Tweet, Toot
)

import pytest
import json

import tweepy

from base64 import b64encode
import requests

import httpretty


def test_twitter_timeline():
    """
    We can mock the calls using https://github.com/gabrielfalcao/HTTPretty
    """
    httpretty.enable(verbose=True, allow_net_connect=False)
    httpretty.register_uri(httpretty.GET, "https://api.twitter.com/2/users/me",
                           body="""{'data':{'id': '123123123','name': 'john','username': 'johnyhon'}}""",
                           status=200)

    httpretty.register_uri(httpretty.GET, "https://api.twitter.com/2/users/123123123/mentions",
                           body="""{'data':[
                            {
                                'id': '111111',
                                'edit_history_tweet_ids': [
                                    '111111'
                                ],
                                'text': '@johnyhon hello'
                                
                                
                                """)

    pass

def test_mastodon_timeline():
    pass

if __name__ == "__main__":
    test_twitter_timeline()