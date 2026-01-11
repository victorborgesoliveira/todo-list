from datetime import datetime, UTC
import json
from models.task import Task

filename = 'db.json'


def main():
    setupDB()
    print('Welcome to todo list app')
    menu()


def menu():
    print('1 - Create task \n'
          '9 - Exit')
    option = input('Choose a option: ')

    if (option == '1'):
        createTask()
        return menu()
    if (option == '9'):
        return print('Closing program')
    print('Invalid option')
    menu()


def listTask():
    readDB()


def createTask():
    description = input('Add task description:')
    status = 'created'
    created_at = datetime.now(UTC)
    task = Task(status=status, created_at=created_at, description=description)
    saveDB(task)


def readDB():
    with open(filename) as f:
        data = json.load(f)
        return data


def saveDB(task: Task):
    data = readDB()
    data.append(task.to_dict())
    with open(filename, "w") as f:
        json.dump(data, f)
        return


def setupDB():
    try:
        with open(filename):
            print('Database already created')
    except FileNotFoundError:
        with open(filename, "x") as f:

            json.dump([], f)
            print('Database created')


main()
