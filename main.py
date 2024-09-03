import datetime
import keyboard

class List:
    tasks = []
    @staticmethod
    def add_task():
        title = input("Pls enter a title for task: ")
        description = input("Pls enter description of task: ")
        tag = input("Enter a tag")
        date = datetime.datetime.now()
        priority = input("pls enter priority for this task: ")

        return Task(title, description, tag, date, priority)

    @staticmethod
    def view_tasks():
        for items in List.tasks:
            print(f'{items.title} | {items.description} | {items.date}\n')


class Task:
    def __init__(self, title, description, tag, date, priority, status="ongoing"):
        self.title = title
        self.description = description
        self.tag = tag
        self.status = status
        self.date = date
        self.priority = priority

        List.tasks.append(self)


if __name__ == '__main__':
    List.add_task()
    List.add_task()
    print('WELCOME TO THE TODO CLI App')
    print('-'*30)
    List.view_tasks()
    print('-'*30)
    print('Press q to quit')
    while True:
        if keyboard.is_pressed('q'):
            print('closing program')
            break   