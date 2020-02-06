#!/usr/bin/python3
""" Contains the function recurse(subreddit, hot_list=[]) """
import requests


def recurse(subreddit, hot_list_titles=[], after='null'):
    """ returns a list containing the titles
    of all hot articles for a given subreddit.
    """
    base_url = 'https://www.reddit.com/r/'
    url = base_url + subreddit + "/hot.json"
    credentials = {'User-Agent': "linux:1:v1.0 (by /u/svelezg_r)"}
    parameters = {"limit": "75", "after": after}
    response = requests.get(url,
                            headers=credentials,
                            params=parameters,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    hot_list_of_dicts = response.json().get("data").get("children")
    after = response.json().get("data").get("after")
    """""to print the after string, which acts as a "pointer"
    to the next response uncomment the following line"""
    # print(after)
    hot_list_titles.extend([reddit.get("data").get("title") for
                            reddit in hot_list_of_dicts])
    """to print the length of the hot_list_titles uncomment
    the following line"""
    # print(len(hot_list_titles))
    if after is None:
        return hot_list_titles
    else:
        return recurse(subreddit, hot_list_titles, after)
