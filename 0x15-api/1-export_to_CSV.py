#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys


def fetch_user_data(user_id):
    """Fetches user data from the API and returns it as a dictionary."""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    return response.json()


def fetch_todos(user_id):
    """Fetches to-do list items for a given user ID from the API and returns them as a list."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": user_id})
    return response.json()


def write_todos_to_csv(user_id, username, todos):
    """Writes the given to-do list items to a CSV file."""
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id, username, todo.get("completed"), todo.get("title")])


def main():
    """Main function of the script."""
    # Get the user ID from the command-line arguments provided to the script
    user_id = sys.argv[1]

    # Fetch user information from the API
    user_data = fetch_user_data(user_id)

    # Extract the username from the user data
    username = user_data.get("username")

    # Fetch the to-do list items associated with the given user ID
    todos = fetch_todos(user_id)

    # Write each item's details (user ID, username, completion status, and title) as a row in the CSV file
    write_todos_to_csv(user_id, username, todos)


if __name__ == "__main__":
    main()
