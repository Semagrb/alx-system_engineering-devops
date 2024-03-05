# 🚀 0x16. API Advanced: Reddit API Exploration 🤖

Welcome aboard, fellow adventurers! Today, we're embarking on a thrilling journey into the depths of the Reddit API using Python. Buckle up and prepare to master the art of API wizardry, where we'll unlock the secrets of reading documentation, navigating pagination, parsing JSON results, making recursive API calls, and even sorting dictionaries. Let's dive in!

## Table of Contents 📚

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Getting Started](#getting-started)
4. [API Documentation](#api-documentation)
5. [Pagination](#pagination)
6. [Parsing JSON Results](#parsing-json-results)
7. [Recursive API Calls](#recursive-api-calls)
8. [Sorting a Dictionary by Value](#sorting-a-dictionary-by-value)
9. [Conclusion](#conclusion)

## Introduction 🎉

Ahoy, mateys! The Reddit API be a treasure trove of digital booty, offering savvy swashbucklers like ourselves the chance to plunder data straight from the seven seas of subreddits. In this escapade, we'll unlock the secrets of the Reddit API, from pagination to parsing, and everything in between. Avast ye, and let's set sail!

## Prerequisites 🏴‍☠️

- Basic understanding of Python 🐍
- Familiarity with the Requests module for sending HTTP requests 📡

## Getting Started 🚀

First mate, prepare the ship! Install the Requests module if ye haven't already:

```bash
pip install requests
```

Then, hoist the Jolly Roger and import the necessary modules into yer Python script:

```python
import requests
import json
```

## API Documentation 📜

To chart our course through the Reddit API, we must consult the sacred scrolls of documentation. Find them at: [Reddit API Documentation](https://www.reddit.com/dev/api/)

To discover the treasures we seek, we'll deploy the `requests.get()` function to send HTTP missives to the Reddit API.

## Pagination 📖

Arr, many an API endpoint supports pagination, allowing us to plunder a limited bounty of results at a time. To navigate the treacherous waters of pagination, we'll wield the before and after query parameters like seasoned buccaneers.

For example, to seize the top 10 posts from the "learnprogramming" subreddit, we'll unfurl the sails with code like this:

```python
url = "https://www.reddit.com/r/learnprogramming/top.json?limit=10"
response = requests.get(url)
data = response.json()

for post in data["data"]["children"]:
    print(post["data"]["title"])
```

## Parsing JSON Results 🧩

The Reddit API bestows its treasures upon us in the form of JSON booty. To decode these arcane messages, we'll call upon the powers of the `json` module in Python.

For instance, to seize the titles of the top 10 posts from the "learnprogramming" subreddit, we'll decode the secrets thusly:

```python
url = "https://www.reddit.com/r/learnprogramming/top.json?limit=10"
response = requests.get(url)
data = response.json()

for post in data["data"]["children"]:
    print(post["data"]["title"])
```

## Recursive API Calls 🔁

Some API quests require a daring adventure through recursive calls to gather all the booty we seek. For example, to plunder all the top 10 posts from the "learnprogramming" subreddit, we'll embark on a perilous journey like so:

```python
def get_top_posts(subreddit, limit=10, after=None):
    url = f"https://www.reddit.com/r/{subreddit}/top.json?limit={limit}"
    if after:
        url += f"&after={after}"
    response = requests.get(url)
    data = response.json()

    posts = []
    for post in data["data"]["children"]:
        posts.append(post["data"]["title"])

    if len(posts) < limit:
        return posts
    else:
        return posts + get_top_posts(subreddit, limit, data["data"]["after"])

top_posts = get_top_posts("learnprogramming")
for post in top_posts:
    print(post)
```

## Sorting a Dictionary by Value 📊

To arrange our plundered loot in order, we must learn the art of sorting a dictionary by its value. Fear not, for this be a task fit for even the most cunning of scallywags.

```python
# To sort a dictionary by value
# Yarrr! Coming soon to a README near you!
```

## Conclusion ⚓️

And there you have it, fellow adventurers! With the wind in our sails and the Reddit API at our fingertips, we've navigated the treacherous waters of API exploration. May your code be as sturdy as a pirate ship and your adventures as legendary as Blackbeard himself. Until next time, fair winds and following seas! 🌊
