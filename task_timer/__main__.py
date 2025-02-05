import click
import time

class TaskTimer:
    def __init__(self):
        self.tasks = {}
        self.current_task = None
        self.start_time = None

    def start_task(self, task_name):
        if self.current_task:
            print(f"Error: Task '{self.current_task}' is already running. Stop it first.")
            return
        self.current_task = task_name
        self.start_time = time.time()
        print(f"Started task: {task_name}")

    def stop_task(self):
        if not self.current_task:
            print("Error: No task is currently running.")
            return
        elapsed_time = time.time() - self.start_time
        if self.current_task in self.tasks:
            self.tasks[self.current_task] += elapsed_time
        else:
            self.tasks[self.current_task] = elapsed_time
        print(f"Stopped task: {self.current_task}, Time spent: {elapsed_time:.2f} seconds")
        self.current_task = None
        self.start_time = None

    def show_summary(self):
        print("Time Sheet Summary:")
        for task, duration in self.tasks.items():
            print(f"{task}: {duration:.2f} seconds")

    def current_running_task(self):
        if self.current_task:
            print(f"Current running task: {self.current_task}")
        else:
            print("No task is currently running.")

def main():
    timer = TaskTimer()
    while True:
        command = input("Enter command (start [task], stop, summary, current): ").strip().lower()
        if command.startswith("start"):
            _, task_name = command.split(" ", 1)
            timer.start_task(task_name)
        elif command == "stop":
            timer.stop_task()
        elif command == "summary":
            timer.show_summary()
        elif command == "current":
            timer.current_running_task()
        else:
            print("Invalid command.")

# need to make the task imbedded into memory in case user exits the class
# need to add clear directions for user at beginning, more print statements explaining
# need to add ability to time two concurrent tasks (extension)
# make docstrings

if __name__ == '__main__':
    main()