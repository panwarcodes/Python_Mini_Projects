# TO-DO List Maker CLI by @panwarcodes/github
import sys
import time

list_of_tasks = []

# Check if tasks.txt exists if not create one
# If exists then read data into list
try:
    with open("tasks.txt", "r") as tasks:
        list_of_tasks = tasks.read().split('\n')
except FileNotFoundError:
    with open("tasks.txt", "w") as tasks:
        pass

# Neccesary functions
def add_task():
    try:
        task = str(input("Enter the task: "))
        list_of_tasks.append(task)
        # Task appending in tasks.txt file as well
        with open("tasks.txt", 'w') as tasks:
            for item in list_of_tasks:
                tasks.write(item + '\n')
        print("Task added!")
    except ValueError:
        print("Only strings are allowed!")

def view_task():
    for index, item in enumerate(list_of_tasks):
        print(f"{index}: {item}")

def remove_task():
    view_task()
    try:
        task = int(input("Enter task's index number: "))
        list_of_tasks.pop(task)
        # Task removing in tasks.net file as well
        with open("tasks.txt", 'w') as tasks:
            for item in list_of_tasks:
                tasks.write(item + '\n')
        print("Task removed!")
    except ValueError:
        print("Only integers are allowed!")

def exit_app():
    sys.exit()

# Welcome interface
while True:
    print("TO-DO List Maker")
    print("""1. Add a task\n2. Remove a task\n3. View all tasks\n4. Exit""")
    print("Loading...")
    time.sleep(1)
    try:
        choice = int(input("Pick option - [ 1,2,3,4 ] (integer only): "))
    except ValueError:
        print("Only integers are allowed!")

    # Choice logic
    match choice:
        case 1:
            add_task()
        case 2:
            remove_task()
        case 3:
            view_task()
        case 4:
            exit_app()