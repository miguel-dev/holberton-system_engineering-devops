#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    url = 'http://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'Miguel'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if not (r.status_code == requests.codes.ok):
        return 0
    else:
        reddit_info = r.json()
        return reddit_info.get("data").get('subscribers')
