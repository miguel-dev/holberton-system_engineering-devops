#!/usr/bin/python3
"""Accepts employee ID and records all tasks in CSV format"""
import csv
import requests
import sys
if __name__ == "__main__":
    url_base = 'https://jsonplaceholder.typicode.com/'
    user = requests.get('{}users/{}'.format(url_base, sys.argv[1]))
    dict_user = user.json()

    tasks = requests.get('{}todos?userId={}'.format(url_base, sys.argv[1]))
    list_tasks = tasks.json()

    with open('{}.csv'.format(sys.argv[1]), mode='w') as csv_file:
        fieldnames = ["USER_ID",
                      "USERNAME",
                      "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csv_file,
                                fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for task in list_tasks:
            writer.writerow({"USER_ID": task.get("userId"),
                             "USERNAME": dict_user.get("username"),
                             "TASK_COMPLETED_STATUS": task.get("completed"),
                             "TASK_TITLE": task.get("title")})
