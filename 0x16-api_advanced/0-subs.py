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
        
        # Check 5: Ensure the response is of the correct type (a dictionary)
        if not isinstance(data, dict):
            return 0
        
        # Check 6: Ensure the 'kind' key exists in the response dictionary
        if 'kind' not in data:
            return 0
        
        # Check 7: Ensure the 'data' key exists in the response dictionary and is a dictionary itself
        if 'data' not in data or not isinstance(data['data'], dict):
            return 0
        
        # Check 8: Ensure the 'subscribers' key exists in the 'data' dictionary and is an integer
        if 'subscribers' not in data['data'] or not isinstance(data['data']['subscribers'], int):
            return 0
        
        return data['data']['subscribers']
    except (requests.exceptions.HTTPError, requests.exceptions.Timeout) as err:
        return 0
