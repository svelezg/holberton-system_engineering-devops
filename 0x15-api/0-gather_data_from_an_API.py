#!/usr/bin/python3
""" for a ann employee ID, returns information about the to-do list progress"""
import json
import requests
import sys

if __name__ == "__main__":
    response_1 = requests.get("https://jsonplaceholder.typicode.com/users/" +
                              sys.argv[1])
    users_dictionary = json.loads(response_1.text)
    employee_name = users_dictionary.get('name')
    response_2 = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                              "?userId=" + sys.argv[1])
    all_task = json.loads(response_2.text)
    task_done = [task for task in all_task if task.get('completed')]
    
    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, len(task_done), len(all_task)))
    for task in task_done:
        print('\t {}'.format(task.get('title')))
