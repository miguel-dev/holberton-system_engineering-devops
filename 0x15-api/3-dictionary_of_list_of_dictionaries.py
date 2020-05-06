#!/usr/bin/python3
"""Accepts employee ID and records all tasks in CSV format"""
import csv
import json
import requests
import sys
if __name__ == "__main__":
    url_base = 'https://jsonplaceholder.typicode.com/'
    users = requests.get('{}users/'.format(url_base))
    list_users = users.json()

    data = {}
    for user in list_users:
        tasks = requests.get('{}todos?userId={}'.format(url_base,
                                                        user.get("id")))
        list_tasks = tasks.json()

        user_data = []
        for task in list_tasks:
            user_data.append({"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": user.get("username")})

        data[user.get("id")] = user_data

    with open('todo_all_employees.json', mode='w') as json_file:
        json.dump(data, json_file)
