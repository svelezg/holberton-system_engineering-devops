#!/usr/bin/python3
""" Contains the function count_words(subreddit, word_list)) """
import requests


def count_words(subreddit, word_list, hot_list_titles=[], after='null'):
    """ returns a list containing the titles
    of all hot articles for a given subreddit.
    """
    base_url = 'https://www.reddit.com/r/'
    url = base_url + subreddit + "/hot.json"
    credentials = {'User-Agent': "linux:1:v1.0 (by /u/svelezg_r)"}
    parameters = {"limit": "100", "after": after}
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
        to_print_tuples = []
        for word in word_list:
            count = 0
            if word.lower() not in [element[0].lower()
                                    for element in to_print_tuples]:
                for title in hot_list_titles:
                    split_title = title.split()
                    new_split = [element.lower() for element in split_title]
                    count = count + new_split.count(word.lower())
            if count != 0:
                to_print_tuples.append((word, count))
        for elem in sorted(to_print_tuples, key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(elem[0], elem[1]))
    else:
        return count_words(subreddit, word_list,
                           hot_list_titles, after)
