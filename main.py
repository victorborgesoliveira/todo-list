from datetime import datetime, UTC

def main():
    createTask()

def createTask():
    description = input('Add task description:')
    status = 'created'
    created_at = datetime.now(UTC)
    print('new task added: ' + description + ', with status: ' + status)
main() 