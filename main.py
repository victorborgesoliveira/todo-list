from datetime import datetime, UTC
from models.task import Task

def main():
    setupDB()
    createTask()

def createTask():
    description = input('Add task description:')
    status = 'created'
    created_at = datetime.now(UTC)
    task = Task(status=status, created_at=created_at, description=description)
    print(task)
def setupDB():
    filename = 'db.json'
    try:
        with open(filename): 
            print('Database already created')
    except FileNotFoundError:
        with open(filename, "x"):
            print('Database created')

main() 
