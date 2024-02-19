#!/usr/bin/python3
"""
Retrieves and displays the to-do list information for a given employee ID.

Usage: python3 todo_list.py <employee_id>
"""

import requests
import sys


def fetch_user_info(employee_id):
    """Fetches user information from the JSONPlaceholder API."""
    base_url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(base_url + "users/{}".format(employee_id))
    return response.json()


def fetch_todo_list(employee_id):
    """Fetches the to-do list for the given employee ID from the JSONPlaceholder API."""
    base_url = "https://jsonplaceholder.typicode.com/"
    params = {"userId": employee_id}
    response = requests.get(base_url + "todos", params=params)
    return response.json()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_list.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        user_info = fetch_user_info(employee_id)
        todo_list = fetch_todo_list(employee_id)

        completed_tasks = [task["title"] for task in todo_list if task["completed"]]

        print("Employee {} has completed {}/{} tasks:".format(user_info["name"], len(completed_tasks), len(todo_list)))

        for task in completed_tasks:
            print("\t", task)

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        sys.exit(1)
