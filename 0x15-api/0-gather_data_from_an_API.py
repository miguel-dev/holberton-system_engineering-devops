#!/usr/bin/python3
"""Scripts using this REST API: https://jsonplaceholder.typicode.com.
Accepts an employeeID returns information about his/her TODO list progress"""

import json
import requests
import sys
list_users = requests.get('https://jsonplaceholder.typicode.com/users').json()
list_tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()
for user in list_users:
    if (user.get('id') == int(sys.argv[1])):
        print("Employee {} is done with".format(user.get('name')), end="")
tasks = []
total = 0
done = 0
for task in list_tasks:
    if (task.get('userId') == int(sys.argv[1])):
        if task.get('completed') is True:
            tasks.append(task.get('title'))
            done += 1
        total += 1
print(" tasks({:d}/{:d}):".format(done, total))
for task in tasks:
    print("\t {}".format(task))
