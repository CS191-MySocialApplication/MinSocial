from requests_oauthlib import OAuth2Session

import json

import urllib.parse

import requests


class TwtAuthHandler():
    def __init__(self, code = None):

        with open("config.json", "r", encoding="utf-8") as config_file:
            configs = json.loads(config_file.read())

        self.redirect_uri = "http://127.0.0.1:5000/logged"
        self.response_type = "code"
        self.client_id = configs["twitter_client_id"]
        self.scope = ["tweet.read", "tweet.write", "users.read", "follows.read", "offline.access", "dm.read"]
        self.state = "state"
        self.code_challenge = "challenge"
        self.code_challenge_method = "plain"
        self.code = code


    def get_auth_url(self):
        url = "https://twitter.com/i/oauth2/authorize?"
        parameters = {
            "redirect_uri": self.redirect_uri,
            "response_type": self.response_type,
            "client_id": self.client_id,
            "scope": " ".join(self.scope),
            "state": self.state,
            "code_challenge": self.code_challenge,
            "code_challenge_method": self.code_challenge_method
        }

        return url + urllib.parse.urlencode(parameters)


    def get_tokens(self):
        assert(self.code != None)

        url = "https://api.twitter.com/2/oauth2/token"

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
        dataToSend = {
            "code": self.code,
            "grant_type":"authorization_code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "code_verifier": "challenge"
        }
        
        r = requests.post(url, headers=headers, data=dataToSend)

        assert(r.status_code == 200)

        return r.json()
    
    def revoke_tokens(self, accessToken=None, refreshToken=None):
        url = "https://api.twitter.com/2/oauth2/revoke"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        formData = {
            "client_id": self.client_id,
            "token": "",
            "token_type_hint": "access_token"
        }

        if accessToken:
            formData["token"] = accessToken
            requests.post(url, headers=headers, data=formData)

        if refreshToken:
            formData["token"] = refreshToken
            requests.post(url, headers=headers, data=formData)

    def refresh_access_token(self, refreshToken):
        url = "https://api.twitter.com/2/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        
        dataToSend = {
            "refresh_token": refreshToken,
            "grant_type":"refresh_token",
            "client_id": self.client_id,
        }

        r = requests.post(url, headers=headers, data=dataToSend)
        return r.json()


class MstdnAuthHandler():
    def __init__(self, code = None):

        with open("config.json", "r", encoding="utf-8") as config_file:
            configs = json.loads(config_file.read())

        self.redirect_uri = "http://127.0.0.1:5000/mstdn/logged"
        self.response_type = "code"
        self.client_id = configs["mastodon_client_id"]
        self.client_secret = configs["mastodon_client_secret"]
        self.scope = ["read","write","follow"]
        self.state = "state"
        self.force_login = "true"
        self.code = code


    def get_auth_url(self):
        url = "https://social.up.edu.ph/oauth/authorize?"
        parameters = {
            "redirect_uri": self.redirect_uri,
            "response_type": self.response_type,
            "client_id": self.client_id,
            "scope": " ".join(self.scope),
            "force_login":"true"
        }

        return url + urllib.parse.urlencode(parameters)


    def get_tokens(self):
        assert(self.code != None)

        url = "https://social.up.edu.ph/oauth/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
        dataToSend = {
            "code": self.code,
            "grant_type":"authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "scope": " ".join(self.scope),
        }
        
        r = requests.post(url, headers=headers, data=dataToSend)

        assert(r.status_code == 200)

        return r.json()
    
    def revoke_tokens(self, accessToken):
        url = "https://social.up.edu.ph/oauth/revoke"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        if accessToken is not None:

            dataToSend = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "token":accessToken,
            }

            r = requests.post(url, headers=headers, data=dataToSend)