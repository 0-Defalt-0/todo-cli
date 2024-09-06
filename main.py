import datetime
import os

class List:
    tasks = []
    @staticmethod
    def add_task():
        id = input("Enter a temp id: ")
        title = input("Pls enter a title for task: ")
        date = datetime.datetime.now()
        priority = input("pls enter priority for this task: ")

        return Task(id, title, date, priority)

    @staticmethod
    def spacing_algo(text, t):
        length = int(len(text))
        total_length = t
        total_spaces = int((total_length - length)/2)
        if (total_length - length) % 2 != 0:
            return ' ' * total_spaces + text + ' ' * (total_spaces+1)
        return ' ' * total_spaces + text + ' ' * total_spaces

    @staticmethod
    def view_tasks():
        print('-'*65)
        print("|  id  "+"|"+" "*20+"task"+" "*20+"|"+" "*2+"priority"+" "*1+"|")
        print('-'*65)
        id_spaces = 6
        task_spaces = 44
        priority_spaces = 11
        for items in List.tasks:
            print('|' + List.spacing_algo(f"{items.id}", id_spaces)+'|'+List.spacing_algo(f"{items.title}", task_spaces)+'|'+List.spacing_algo(f"{items.priority}", priority_spaces)+'|')
            print('-'*65)

class Task:
    def __init__(self, id, title, date, priority="High", status="ongoing"):
        self.id = id
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
            os.system('cls')
            break