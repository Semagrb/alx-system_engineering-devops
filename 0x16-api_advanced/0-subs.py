#!/usr/bin/python3

"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If not a valid subreddit, returns 0.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'my-reddit-api-client'}
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get('kind') == 't5':
            return data['data'].get('subscribers', 0)
        else:
            return 0
    except (requests.exceptions.HTTPError, requests.exceptions.Timeout) as err:
        return 0
