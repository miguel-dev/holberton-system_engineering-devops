#!/usr/bin/python3
"""Accepts employee ID and records all tasks in CSV format"""
import csv
import json
import requests
import sys
if __name__ == "__main__":
    url_base = 'https://jsonplaceholder.typicode.com/'
    user = requests.get('{}users/{}'.format(url_base, sys.argv[1]))
    dict_user = user.json()

    tasks = requests.get('{}todos?userId={}'.format(url_base, sys.argv[1]))
    list_tasks = tasks.json()

    data = {}
    list_data = []
    for task in list_tasks:
        list_data.append({"task": task.get("title"),
                          "completed": task.get("completed"),
                          "username": dict_user.get("username")})
    data[task.get("userId")] = list_data

    with open('{}.json'.format(sys.argv[1]), mode='w') as json_file:
        json.dump(data, json_file)
