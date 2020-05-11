#!/usr/bin/python3
"""
Queries Reddit API and returns a list of all the hot posts
a given subreddit. If not results are found, return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Prints titles of first hot posts of a given subreddit"""
    url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    headers = {'user-agent': 'Miguel'}
    params = {'after': after}
    r = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if (r.status_code != requests.codes.ok):
        return('None')
    else: 
        dict_hot = r.json()
        hot_posts = dict_hot.get("data").get('children')
        if len(hot_posts) > 0:
            hot_list.extend(hot_posts)
        after = dict_hot.get('data').get('after')
        if not after:
            return hot_list
        else:
            recurse(subreddit, hot_list, after)
