#!/usr/bin/python3
"""
Queries Reddit API and prints the titles of the first 10 hot posts
a given subreddit
"""
import requests


def top_ten(subreddit):
    """Prints titles of first 10 hot posts of a given subreddit"""
    url = 'https://reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'user-agent': 'linux:api_advanced:v1.2 (by /u/miguel-dev)'}
    r = requests.get(url, headers=headers)
    if not (r.status_code == requests.codes.ok):
        print('None')
    else:
        dict_hot = r.json()
        hot_posts = dict_hot.get("data").get('children')
        for post in hot_posts:
            print(post.get('data').get('title'))
