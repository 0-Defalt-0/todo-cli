import datetime
import os

class List:
    tasks = []
    @staticmethod
    def add_task():
        title = input("Pls enter a title for task: ")
        date = datetime.datetime.now()
        priority = input("pls enter priority for this task: ")

        return Task(title, date, priority)

    @staticmethod
    def view_tasks():
        for items in List.tasks:
            print(f'{len(items.title) * "-"}')
            print(items.title)


class Task:
    def __init__(self, title, date, priority="High", status="ongoing"):
        self.title = title
        self.status = status
        self.date = date
        self.priority = priority

        List.tasks.append(self)


if __name__ == '__main__':
    print('-'*65)
    print("|  id  "+"|"+" "*20+"task"+" "*20+"|"+" "*2+"priority"+" "*1+"|")
    print('-'*65)

    # command center
    while True:
        print('\n\n')
        user_input = input('.todo: ') 
        if user_input == 'add_task':
            List.add_task()
            os.system('cls')
            List.view_tasks()
        elif user_input == 'view_tasks':
            List.view_tasks()
        elif user_input == '/quit':
            break