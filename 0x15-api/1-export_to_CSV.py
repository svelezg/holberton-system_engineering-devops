#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
Extension script to export data in the CSV format.
"""
if __name__ == "__main__":
    import csv
    import requests
    import sys

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'

    url = base_url + 'users/' + employee_id
    response = requests.get(url)

    # username of the employee
    employee_name = response.json().get('username')

    url = base_url + 'todos'
    response = requests.get(url)

    # "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    tasks = [task for task in response.json()
             if task.get('userId') is int(employee_id)]

    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        fields = ["userId", "name", "completed", "title"]
        writer = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL)
        for task in tasks:
            task['name'] = employee_name
            del task['id']
            writer.writerow(task)
