
__version__ = "0.1.0"
import sys
import logging
import os

class UserFilter(logging.Filter):
    def __init__(self,user):
        super().__init__()
        self.user = user
    def filter(self, record):
        record.user = self.user
        return True
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        with open('todo.txt', 'a') as f:
            f.write(task + '\n')

    def view_tasks(self):
        with open('todo.txt', 'r') as f:
            tasks = f.readlines()
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

    def delete_task(self, task_number):
        with open('todo.txt', 'r') as f:
            tasks = f.readlines()
        del tasks[task_number - 1]
        with open('todo.txt', 'w') as f:
            for task in tasks:
                f.write(task)
def log(name: str, local: str,level:int, message:str):
    log = logging.Logger(name, level)
    fh = logging.FileHandler(local)
    tmp = logging.Formatter("%(asctime)s - %(user)s - %(levelname)s -> %(message)s ")
    fh.setFormatter(tmp)
    log.addHandler(fh)
    user = os.getenv("USER", "anonymous")
    userfilter = UserFilter(user)
    log.addFilter(userfilter)
    if log.level == 10:
        log.debug(message)
    elif log.level == 20:
        log.info(message)
    elif log.level == 30:
        log.warning(message)
    elif log.level == 40:
        log.error(message)
    elif log.level == 50:
        log.critical(message)
arguments = ("new", "delete", "view")
todo = TodoList()
try: 
    argv = sys.argv[1]
    if argv == arguments[0]:
        task = input("digite a tarefa: ")
        todo.add_task(task)
        log("logger", "todo.log", 20,"adicionou uma task")
    if argv == arguments[1]:
        todo.view_tasks()
        indice = input("qual tarefa voce quer eliminar? ")
        todo.delete_task(int(indice))
        log("logger", "todo.log", 20, "deletou uma task")
    if argv == arguments[2]:
        log("logger", "todo.log", 20, "mostrou todas as tasks")
        todo.view_tasks()
except (IndexError) as e:
    log("logger","todo.log",40,"argumento invalido!") 
    print("os argumentos validos sao ('new', 'delete', 'view')")
