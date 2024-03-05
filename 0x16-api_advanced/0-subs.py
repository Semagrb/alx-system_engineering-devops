#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 302:
        return 0  # Redirect encountered, invalid subreddit
    else:
        return 0  # Other errors, such as 404, treat as invalid subreddit

# Test the function
print(number_of_subscribers("programming"))  # Example valid subreddit
print(number_of_subscribers("this_is_a_fake_subreddit"))  # Example invalid subreddit
