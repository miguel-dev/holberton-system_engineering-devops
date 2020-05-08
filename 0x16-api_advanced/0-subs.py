#!/usr/bin/python3
"""
Queries Reddit API and returns number of subscribers for
a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers for given subreddit"""
    url = 'http://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'request'}
    ir = requests.get(url, headers=headers)
    if not (r.status_code == requests.codes.ok):
        return 0
    else:
        reddit_info = r.json()
        return reddit_info.get("data").get('subscribers')
