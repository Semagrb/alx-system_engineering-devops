#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys


def fetch_user_data(employee_id):
    """Fetch user information and to-do list for a given employee ID."""
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get the employee information using the provided employee ID
    user_url = base_url + "users/{}".format(employee_id)
    user_response = requests.get(user_url)
    user = user_response.json()

    # Get the to-do list for the employee using the provided employee ID
    todo_params = {"userId": employee_id}
    todo_url = base_url + "todos"
    todo_response = requests.get(todo_url, params=todo_params)
    todos = todo_response.json()

    return user, todos


def get_completed_tasks(todos):
    """Filter completed tasks from a given to-do list."""
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    return completed


def print_completed_tasks(completed):
    """Print completed tasks with indentation."""
    for complete in completed:
        print("\t", complete)


if __name__ == "__main__":
    # Get the employee ID from the command-line argument
    employee_id = sys.argv[1]

    # Fetch the user data and to-do list information
    user, todos = fetch_user_data(employee_id)

    # Filter completed tasks and count them
    completed = get_completed_tasks(todos)

    # Print the employee's name and the number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the completed tasks one by one with indentation
    print_completed_tasks(completed)
