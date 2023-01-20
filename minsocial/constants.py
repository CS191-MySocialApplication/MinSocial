TWITTER_CLIENT_ID = "WjRDYmF4eGQxMEpyX2NRM2pQV3E6MTpjaQ"


### === AUTH ===
GET_AUTH = {
    "URL":"https://twitter.com/i/oauth2/authorize?",
    "PARAMS":{"response_type":"code",
    "client_id": TWITTER_CLIENT_ID,
    "redirect_uri":"http://127.0.0.1:5000/logged",
    "scope":"tweet.read users.read follows.read offline.access dm.read",
    "state":"state",
    "code_challenge":"challenge",
    "code_challenge_method":"plain"} 
}

POST_TOKEN = {
    "URL":"https://api.twitter.com/2/oauth2/token",
    "HEADER":{"Content-Type": "application/x-www-form-urlencoded"},
    "DATA":{
        "code": "",
        "grant_type":"authorization_code",
        "client_id": TWITTER_CLIENT_ID,
        "redirect_uri": "http://127.0.0.1:5000/logged",
        "code_verifier": "challenge"
    }
}

POST_REFRESH = {
    "URL":"https://api.twitter.com/2/oauth2/token",
    "HEADER":{"Content-Type": "application/x-www-form-urlencoded"}
}

POST_LOGOUT_ACCESS = {
    "URL":"https://api.twitter.com/2/oauth2/revoke",
    "HEADER":{"Content-Type": "application/x-www-form-urlencoded"},
    "DATA":{
            "client_id": TWITTER_CLIENT_ID,
            "token": "",
            "token_type_hint": "access_token"
    }
}

POST_LOGOUT_REFRESH = {
    "URL":"https://api.twitter.com/2/oauth2/revoke",
    "HEADER":{"Content-Type": "application/x-www-form-urlencoded"},
    "DATA":{
            "client_id": TWITTER_CLIENT_ID,
            "token": "",
            "token_type_hint": "refresh_token"
    }
}

### === QUERIES ===
GET_MENTIONED = {
    "URL":"https://api.twitter.com/2/users/{}/mentions",
    "HEADER": {
        "Authorization" : "Bearer {}"
    }
}

GET_DMS = {
    "URL":"https://api.twitter.com/2/dm_events?dm_event.fields=id,text,sender_id",
    "HEADER":{
        "Authorization" : "Bearer {}"
    }
}

GET_USER = {
    "URL":"https://api.twitter.com/2/users/{}",
    "HEADER":{
        "Authorization" : "Bearer {}"
    }
}

GET_ME = {
    "URL":"https://api.twitter.com/2/users/me",
    "HEADER":{
        "Authorization" : "Bearer {}"
    }
}

GET_TWEET = {
    "URL": "https://api.twitter.com/2/tweets/{}",
    "HEADER":{
        "Authorization" : "Bearer {}"
    }
}