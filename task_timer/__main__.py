"""
Program: Task Timer
Class: CS 314
Date: 06-Feb-2025
Author: Kaylee Hinton
Descripton: This task timer will be able to start and stop currently running tasks
while also being able to allow the tracking of concurrent tasks and include color in the output console
"""

import time
from colorama import Fore, Back, Style

class TaskTimer:
    """ This class allows a user to create and track multiple concurrent tasks, with the ability to stop
    a specific or multiple tasks. The class also allows for the user to track currently running tasks and 
    record a list of completed tasks. 
    
    """

    def __init__(self):
        self.tasks = {}
        self.running_tasks = {}

    def start_task(self, task_name):
        """ Allows for a task with a user given name to be created and start recording its time """

        if task_name in self.running_tasks:
            print()
            print(Fore.RED + 'Error')
            print(f"Task '{task_name}' is already running.")
            return

        # starting_time = datetime.datetime.now().strftime("%H:%M:%S")
        # print(starting_time)
        
        self.running_tasks[task_name] = time.time()
        print()
        print(Fore.GREEN + 'Started Task')


    def stop_task(self, task_name):
        """ Allows for a task with a user given name to be stopped and give its elasped time """
        
        if not task_name:
            print(Fore.RED + 'Error: Please specifiy a task name')
            return
        
        if task_name not in self.running_tasks:
            print(Fore.RED + 'Error: No task with that name currently running')
            return
        

        elapsed_time = time.time() - self.running_tasks.pop(task_name)
        if task_name in self.running_tasks:
            self.tasks[task_name] += elapsed_time
        else:
            self.tasks[task_name] = elapsed_time

        print()
        print(Fore. RED + 'Stopped Task')
        print(f"Time spent: {elapsed_time:.2f} seconds")


    def show_summary(self):
        """ Creates a list of all tasks that were completed """

        print(Fore.CYAN + 'Time Sheet Summary:')
        for task, duration in self.tasks.items():
            print(f"{task}: {duration:.2f} seconds")


    def current_running_task(self):
        """ Creates a list of all tasks that are currently being timed """

        if self.running_tasks:
            print(Fore.GREEN + 'Current Running Tasks')
            for task, duration in self.running_tasks.items():
                print(f"{task}: {duration: .02f} seconds")

        else:
            print(Fore.RED + 'No Task is currently running')


def main():
    """ User-driven menu that allows the user to utilize all the parts of the task timer class """
    timer = TaskTimer()
    print()
    print(Fore.GREEN + 'Use the commands below to start or stop a task/tasks, to see currently running tasks, a task summary, a help menu, or to exit the program')

    while True:
        print()
        command = input("Enter command (Start [task], Stop [task], Summary, Current, Help, Exit): ").lower()
        if command.startswith("start"):
            _, task_name = command.split(" ", 1)
            timer.start_task(task_name)

        elif command.startswith("stop"):
            _, task_name = command.split(" ", 1)
            timer.stop_task(task_name)

        elif command == "summary":
            timer.show_summary()

        elif command == "current":
            timer.current_running_task()

        elif command == "help":
            print(Fore.YELLOW + 'List of available commands')
            print(Fore.GREEN + 'Start [task name]: Starts the timer for a task with a given name') 
            print(Fore.RED + 'Stop [task name]: Stops the timer for a task with a given name')
            print(Fore.CYAN + 'Summary: Prints a list of completed tasks')
            print(Fore.GREEN + 'Current: Prints a list of currently running tasks')
            print(Fore.YELLOW + 'Help: displays each command with the descriptions')
            print(Fore.RED + 'Exit: exits the task timer')

        elif command == "exit":
            break
        else:
            print(Fore.RED + 'Invalid command')
            

if __name__ == '__main__':
    main()
