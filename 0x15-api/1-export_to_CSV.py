#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys


def fetch_user_data(user_id, url):
    """Fetch user information and to-do list for a given employee ID."""
    # Get the employee information using the provided employee ID
    user_url = url + "users/{}".format(user_id)
    user_response = requests.get(user_url)
    user = user_response.json()

    # Get the to-do list for the employee using the provided employee ID
    todo_params = {"userId": user_id}
    todo_url = url + "todos"
    todo_response = requests.get(todo_url, params=todo_params)
    todos = todo_response.json()

    return user, todos


def write_to_csv(user_id, username, todos, csvfile):
    """Write to-do list information to a CSV file."""
    # Use list comprehension to iterate over the to-do list items
    # Write each item's details (user ID, username, completion status,
    #   and title) as a row in the CSV file
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]


if __name__ == "__main__":
    # Get the employee ID from the command-line arguments provided to the script
    user_id = sys.argv[1]

    # Define the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch the user data and to-do list information
    user, todos = fetch_user_data(user_id, url)

    # Extract the username from the user data
    username = user.get("username")

    # Create a CSV file with the employee ID as the filename
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        # Write the to-do list information to the CSV file
        write_to_csv(user_id, username, todos, csvfile)
