#!/usr/bin/python3
""" Contains the function ntop_ten(subreddit) """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot
    posts listed for a given subreddit.
    """
    base_url = 'https://www.reddit.com/r/'
    url = base_url + subreddit + "/hot.json"
    credentials = {'User-Agent': "linux:1:v1.0 (by /u/svelezg_r)"}
    max_number = {'limit': "10"}
    response = requests.get(url,
                            headers=credentials,
                            params=max_number,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
    else:
        hot_list_of_dicts = response.json().get("data").get("children")
        titles = [reddit.get("data").get("title") for
                  reddit in hot_list_of_dicts]
        for title in titles:
            print(title)
