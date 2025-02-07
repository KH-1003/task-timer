# Program: Task Timer
# Class: CS 314
# Date: 06-Feb-2025
# Author: Kaylee Hinton
# Descripton: This task timer will be able to start and stop currently running tasks
# while also being able to allow the tracking of concurrent tasks and include color in the output console

import time

class TaskTimer:
    """Allows the user to start tasks, stop tasks, see currently running tasks, a summary of previously ended tasks
    and to end the function when they are done.
    """
    def __init__(self):
        # History of all the tasks
        self.tasks = {}
        # History of current running tasks
        self.running_tasks = {}

    def start_task(self, task_name):
        """ Takes in a task name and creates a task and starts a designated timer for the task just started """
        if task_name in self.running_tasks:
            # Shows the user there is already a task with that name
            print(f"Error: Task '{task_name}' is already running.")
            return
        # Starts a new task and adds it to the running task dictionary
        self.running_tasks[task_name] = time.time()
        print(f"Started task: {task_name}")

    def stop_task(self, task_name):
        """ Takes in the specified task name and stops the timer with the designated task """
        if not task_name:
            # Shows the user that they did not specify a task
            print("Error: Please specifiy a task name.")
            return
        # No currently running task with that name
        if task_name not in self.running_tasks:
            print(f"Error: No task with that name currently running")
            return
        # Finds the total time that was recorded for that task when it was first started to when it stopped
        elapsed_time = time.time() - self.running_tasks.pop(task_name)
        if task_name in self.running_tasks:
            self.tasks[task_name] += elapsed_time
        else:
            self.tasks[task_name] = elapsed_time
        print(f"Stopped task: {task_name}, Time spent: {elapsed_time:.2f} seconds")


    def show_summary(self):
        """ Prints a complete list of all tasks that were started and stopped """
        print("Time Sheet Summary:")
        for task, duration in self.tasks.items():
            print(f"{task}: {duration:.2f} seconds")


    def current_running_task(self):
        """ Prints a complete list of all the tasks still currently running """
        if self.running_tasks:
            print(f"Current running tasks: {self.running_tasks}")
        else:
            print("No task is currently running.")

def main():
    """Starts the main function and allows the user to access all the features of the class"""
    timer = TaskTimer()
    print(" ")
    print("Use the commands below to start or stop a task/tasks, to see currently running tasks, a task summary, or to exit the program")
    while True:
        print("")
        command = input("Enter command (Start [task], Stop [task], Summary, Current, Exit): ").lower()
        if command.startswith("start"):
            _, task_name = command.split(" ", 1)
            # Calls the function to start a task with the task name
            timer.start_task(task_name)
        elif command.startswith("stop"):
            _, task_name = command.split(" ", 1)
            # Calls the function to stop a task with the task name
            timer.stop_task(task_name)
        elif command == "summary":
            # Calls the function to show the summary of all completed tasks
            timer.show_summary()
        elif command == "current":
            # Calls the function to show the current tasks that are being timed
            timer.current_running_task()
        # Allows the user to exit the program when they are done
        elif command == "exit":
            break
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()