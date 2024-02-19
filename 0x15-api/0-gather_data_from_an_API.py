#!/usr/bin/python3
"""
This script retrieves and displays the to-do list information for a given employee ID.

It takes an employee ID as a command-line argument and fetches the corresponding user information
and to-do list from the JSONPlaceholder API. Then, it prints the tasks completed by the employee.
"""

import requests
import sys

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Extract the employee ID from the command-line argument
    employee_id = sys.argv[1]

    # Retrieve user information for the given employee ID
    user_info = requests.get(base_url + "users/{}".format(employee_id)).json()

    # Retrieve the to-do list for the employee
    todo_list = requests.get(base_url + "todos", params={"userId": employee_id}).json()

    # Filter completed tasks
    completed_tasks = [task["title"] for task in todo_list if task["completed"]]

    # Print employee's name and the number of completed tasks
    print("Employee {} has completed {}/{} tasks:".format(user_info["name"], len(completed_tasks), len(todo_list)))

    # Print the completed tasks
    for task in completed_tasks:
        print("\t", task)
