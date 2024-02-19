#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    # Get the user ID from the command-line arguments provided to the script
    user_id = sys.argv[1]

    # Define the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information from the API and convert the response to a JSON object
    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()

    # Extract the username from the user data
    username = user.get("username")

    # Fetch the to-do list items associated with the given user ID and convert the response to a JSON object
    params = {"userId": user_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()

    # Write to-do list information to a CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Iterate over the to-do list items and write each item's details as a row in the CSV file
        for todo in todos:
            row = [user_id, username, todo.get("completed"), todo.get("title")]
            writer.writerow(row) 
