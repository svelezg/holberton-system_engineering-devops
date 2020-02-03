#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'

    url1 = base_url + 'users/' + employee_id
    response_1 = requests.get(url1, 'name')
    users_dictionary = json.loads(response_1.text)
    employee_name = users_dictionary.get('name')

    url2 = base_url + 'todos/' + "?userId=" + sys.argv[1]
    response_2 = requests.get(url2)
    all_task = json.loads(response_2.text)
    task_done = [task for task in all_task if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, len(task_done), len(all_task)))

    for task in task_done:
        print('\t {}'.format(task.get('title')))
