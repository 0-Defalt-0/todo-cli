import datetime
import os
import math
import json

class List:
    tasks = []
    @staticmethod
    def add_task():
        title = input("Pls enter a title for task: ")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        priority = input("pls enter priority for this task: ")

        return Task(title, date, priority)

    @staticmethod
    def spacing_algo(text, t):
        length = len(text)
        total_length = t
        total_spaces = int((total_length - length)/2)
        if length > total_length:
            # calculate the total lines it would take to fill the text (44 for each line)
            lines = math.ceil(length/44)
            # calculating the spaces that will take to fill the row
            spaces = int((44 * math.ceil(length/44)) - 44*(length/44))
            # first 44 letters of the task
            txt = text[:44] + '|' + ' ' * 11 + '|' + '\n'

            # responsive layout logic
            
            ''' The golden formula
            return text[:total_length] + '|' + ' ' * 11 + '|' + '\n' + '|' + ' ' * 6 + '|' + text[total_length:] + ' ' * spaces
            '''
               
            # calculating remaining text of the task so that it fills up the rows
            for i in range(2, lines):    
                txt += '|' + ' ' * 6 + '|' + text[44*(i-1):44*i] + '|' + ' ' * 11 + '|' + '\n'
            txt += '|' + ' ' * 6 + '|' + text[44*(lines-1):44*lines] + ' ' * spaces
            return txt

        # This prevents the mislayout when the difference is odd
        elif (total_length - length) % 2 != 0:
            return ' ' * total_spaces + text + ' ' * (total_spaces+1)
        # the basic layout if above are not met
        return ' ' * total_spaces + text + ' ' * total_spaces

    @staticmethod
    def view_tasks():
        #loading data from json db
        with open('todo_db.json') as f:
            data = json.load(f)

        print('-'*65)
        print("|  id  "+"|"+" "*20+"task"+" "*20+"|"+" "*2+"priority"+" "*1+"|")
        print('-'*65)
        id_spaces = 6
        task_spaces = 44
        priority_spaces = 11
        for items in data:
            print('|' + List.spacing_algo(f"{items.get('id')}", id_spaces)+'|'+List.spacing_algo(f"{items.get('title')}", task_spaces)+'|'+List.spacing_algo(f"{items.get('priority')}", priority_spaces)+'|')
            print('-'*65)

    def remove_task():
        inp = input('pls enter the id of the task you want to remove: ')
        
        inp = int(inp)
        with open('todo_db.json') as f:
            data = json.load(f)
        
        try:
            new_data = [item for item in data if item.get('id') != inp]

            if len(new_data) == len(data):
                print("Task not found no changes made")
            else:               
                with open('todo_db.json', 'w') as f:
                    json.dump(new_data, f, indent=4)
                os.system('cls')
                List.view_tasks()
        except ValueError:
            print("Invalid input pls enter a numeric id")

class Task:
    # getting unique ids by checking existing from db
    if os.path.exists('todo_db.json'):
        with open('todo_db.json','r') as f:
            try:
                content = f.read()
                data = json.loads(content)
            except:
                data = []
    else:
        data = []

    id = 0
    ids = [items.get('id') for items in data]
    def __init__(self, title, date, priority="High", status="ongoing"):
        if Task.id in Task.ids:
            self.id = max(Task.ids) + 1
        else:
            self.id = Task.id
        self.title = title
        self.status = status
        self.date = date
        self.priority = priority

        # keep increamenting so we get unique ids for each task
        Task.id += 1

        # saving it to the json database
        if os.path.exists('todo_db.json'):
            with open('todo_db.json', 'r') as f:
                try:
                    content = f.read()
                    tasks = json.loads(content)
                except json.JSONDecodeError:
                    tasks = []
        else:
            tasks = []
        
        #append the new task to list
        tasks.append({
            'id':self.id,
            'title':self.title,
            'date':self.date,
            'status':self.status,
            'priority':self.priority
        })

        with open('todo_db.json', 'w') as f:
            json.dump(tasks, f, indent=4)

if __name__ == '__main__':
    List.view_tasks()

    # command center
    while True:
        print('\n\n')
        user_input = input('.todo: ') 
        if user_input == 'add_task':
            List.add_task()
            os.system('cls')
            List.view_tasks()
        elif user_input == 'view_task':
            List.view_tasks()
        elif user_input == 'remove_task':
            List.remove_task()
        elif user_input == '/quit':
            os.system('cls')
            break

