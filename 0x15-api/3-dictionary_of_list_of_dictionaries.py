#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.

This script fetches the user information and to-do lists for all employees
from the JSONPlaceholder API and exports the data to a JSON file.
"""

import json
import requests


def fetch_user_data():
    """Fetch user information and to-do lists for all employees."""
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch the list of all users (employees)
    users = requests.get(base_url + "users").json()

    # Create a dictionary to store the to-do list information of all employees
    data_to_export = {}

    # Iterate through each user (employee)
    for user in users:
        # Get the user ID
        user_id = user["id"]

        # Construct the URL to fetch the to-do list for the current user
        user_url = base_url + f"todos?userId={user_id}"

        # Fetch the to-do list for the current user
        todo_list = requests.get(user_url).json()

        # Create a list to store the to-do list information for the current user
        user_data = []

        # Iterate through each to-do item in the to-do list
        for todo in todo_list:
            # Create a dictionary to store the to-do item information
            todo_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }

            # Append the to-do item information to the list for the current user
            user_data.append(todo_info)

        # Add the to-do list information for the current user to the main data dictionary
        data_to_export[user_id] = user_data

    return data_to_export


if __name__ == "__main__":
    # Fetch the user data and to-do list information
    data_to_export = fetch_user_data()

    # Write the data to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
