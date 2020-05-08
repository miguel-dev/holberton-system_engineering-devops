#!/usr/bin/python3
"""
Queries Reddit API and returns number of subscribers for
a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers for given subreddit"""
    url = 'https://api.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'Miguel'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if (r.status_code != requests.codes.ok):
        return 0
    else:
        reddit_info = r.json()
        return reddit_info.get("data").get('subscribers')
