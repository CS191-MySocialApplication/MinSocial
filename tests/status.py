from minsocial.query.status import (
    Timeline, Tweet, Toot, Status
)

import httpretty


def test_twitter_timeline():
    """
    We can mock the calls using https://github.com/gabrielfalcao/HTTPretty
    """

    with open("tests/simulated_responses/twt_me.json", "r", encoding="utf-8") as me_file:
        me_body = me_file.read()

    with open("tests/simulated_responses/twt_home.json", "r", encoding="utf-8") as test_file:
        test_body = test_file.read()

    httpretty.enable(verbose=True, allow_net_connect=False)
    httpretty.register_uri(httpretty.GET, "https://api.twitter.com/2/users/me",
                           body=me_body,
                           status=200,
                           content_type="text/json")

    httpretty.register_uri(httpretty.GET, "https://api.twitter.com/2/users/994289933354332160/mentions",
                            body=test_body,
                            status=200)
    
    timeline = Timeline(twtAccessKey="sdfsdf")

    assert type(timeline[0]) is Tweet


def test_mastodon_timeline():

    with open("tests/simulated_responses/mstdn_home.json", "r", encoding="utf-8") as test_file:
        test_body = test_file.read()

    with open("tests/simulated_responses/mstdn_instance.json", "r", encoding="utf-8") as instance_file:
        instance_body = instance_file.read()

    httpretty.enable(verbose=True, allow_net_connect=False)
    httpretty.register_uri(httpretty.GET, "https://social.up.edu.ph/api/v1/notifications",
                            body=test_body,
                            status=200)
    
    httpretty.register_uri(httpretty.GET, "https://social.up.edu.ph/api/v1/instance/",
                           body=instance_body,
                           status=200)
    
    timeline = Timeline(mstdnAccessKey="asdasd")

    assert(type(timeline[0]) is Toot)


def test_sorted_timeline():

    with open("tests/simulated_responses/twt_me.json", "r", encoding="utf-8") as me_file:
        me_body = me_file.read()

    with open("tests/simulated_responses/twt_home.json", "r", encoding="utf-8") as test_file:
        twt_test_body = test_file.read()

    with open("tests/simulated_responses/mstdn_home.json", "r", encoding="utf-8") as test_file:
        mstdn_test_body = test_file.read()

    with open("tests/simulated_responses/mstdn_instance.json", "r", encoding="utf-8") as instance_file:
        instance_body = instance_file.read()

    httpretty.enable(verbose=True, allow_net_connect=False)
    httpretty.register_uri(httpretty.GET, "https://api.twitter.com/2/users/me",
                           body=me_body,
                           status=200,
                           content_type="text/json")

    httpretty.register_uri(httpretty.GET, "https://api.twitter.com/2/users/994289933354332160/mentions",
                            body=twt_test_body,
                            status=200)
    
    httpretty.register_uri(httpretty.GET, "https://social.up.edu.ph/api/v1/notifications",
                            body=mstdn_test_body,
                            status=200)
    
    httpretty.register_uri(httpretty.GET, "https://social.up.edu.ph/api/v1/instance/",
                           body=instance_body,
                           status=200)
    
    timeline = Timeline(twtAccessKey="asd", mstdnAccessKey="asdasd")

    assert sorted(timeline.statusList, key=lambda x: x.createdTime, reverse=True) == timeline.statusList

if __name__ == "__main__":
    test_sorted_timeline()