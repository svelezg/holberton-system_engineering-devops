#!/usr/bin/python3
""" Contains the function number_of_subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
    base_url = 'https://www.reddit.com/r/'
    url = base_url + subreddit + "/about.json"
    credentials = {'User-Agent': "carejkhlkhlk"}
    response = requests.get(url, headers=credentials, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data").get("subscribers")
