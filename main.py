from datetime import datetime, UTC

def main():
    setupDB()
    createTask()

def createTask():
    description = input('Add task description:')
    status = 'created'
    created_at = datetime.now(UTC)
    print('new task added: ' + description + ', with status: ' + status)

def setupDB():
    filename = 'db.json'
    try:
        with open(filename): 
            print('Database already created')
    except FileNotFoundError:
        with open(filename, "x"):
            print('Database created')

main() 
