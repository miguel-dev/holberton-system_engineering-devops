#!/usr/bin/python3
"""Accepts employee ID and returns TODO list progress"""
import requests
import sys
if __name__ == "__main__":
    url_base = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url_base + 'users/{}'.format(sys.argv[1]))
    dict_user = user.json()

    tasks = requests.get(url_base + 'todos?userId={}'.format(sys.argv[1]))
    list_tasks = tasks.json()

    num_done = 0
    num_total = 0
    titles = []
    for task in list_tasks:
        if task["completed"] is True:
            num_done += 1
            titles.append(task["title"])
        num_total += 1

    string = 'Employee {} is done with tasks({:d}/{:d}):'
    print(string.format(dict_user["name"], num_done, num_total))
    for title in titles:
        print("\t{}".format(title))
