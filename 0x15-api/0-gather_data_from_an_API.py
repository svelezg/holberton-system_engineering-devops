#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import requests
    import sys

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'

    url = base_url + 'todos'
    response = requests.get(url)
    # print(response.json())

    url = base_url + 'users/' + employee_id
    response_1 = requests.get(url, 'name')

    # name of the employee
    employee_name = response_1.json().get('name')

    # total number of tasks, which is the sum of completed and
    # non-completed tasks
    url = base_url + 'todos'
    response_2 = requests.get(url)

    # number of completed tasks
    task_done = len([task for task in response_2.json()
                     if task.get('userId') is int(employee_id) and
                     task.get('completed') is True])
    task_total = len([task for task in response_2.json()
                      if task.get('userId') is int(employee_id)])

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, task_done, task_total))

    # Second and N next lines display the title of completed tasks:
    # Tab TASK_TITLE (with 1 tabulation + 1 space before)
    for task in response_2.json():
        if task.get('userId') is int(employee_id):
            if task.get('completed') is True:
                print('\t {}'.format(task.get('title')))
