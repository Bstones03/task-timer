"""
task_timr.py
Brennen Stones <brennen.stones@student.cune.edu>
2025-02-06

This holds the class for the Task Timer
all the functions of the task are functions of the class
these are:
Starting and creating the task
stopping and logging the task
allow changing the time each task was done
and printing and exporting the timesheet
"""


import csv
import time
from datetime import datetime
from collections import defaultdict


class TaskTimer:
    def __init__(self):
        self.tasks = defaultdict(list)
        self.current_task = None
        self.start_time = None

    def start_task(self, task_name):
        """starts and creates a single task"""
        if self.current_task:
            #stops the current task if you try to start it again
            print(f"Stopping current task: {self.current_task}")
            self.stop_task()
        self.current_task = task_name
        self.start_time = time.time()
        print(f"Started task: {task_name}")

    def stop_task(self):
        """stops task and records the time"""
        if not self.current_task:
            #no task running
            print("No task is currently running.")
            return
        elapsed_time = time.time() - self.start_time
        self.tasks[self.current_task].append(elapsed_time)
        print(f"Stopped task: {self.current_task} (Duration: {elapsed_time:.2f} seconds)")
        self.current_task = None
        self.start_time = None

    def print_timesheet(self):
        """prints out all tasks created and times recorded
           doesn't print task that hasn't ended"""
        print("\nTimesheet Summary:")
        for task, durations in self.tasks.items():
            total_time = sum(durations)
            print(f"{task}: {len(durations)} entries, Total time: {total_time:.2f} seconds")

    def current_running_task(self):
        """prints out current task that is running"""
        if self.current_task:
            print(f"Current running task: {self.current_task}")
        else:
            print("No task is currently running.")

    def export_timesheet(self, filename='timesheet.csv'):
        """csv print out for all tasks created and times recorded
           doesn't record if task hasn't ended"""
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Task', 'Duration (seconds)'])
            for task, durations in self.tasks.items():
                for duration in durations:
                    writer.writerow([task, duration])
        print(f"Timesheet exported to {filename}")

    def edit_timesheet(self, task_name, new_duration):
        """allows changing time recorded for a task"""
        if task_name in self.tasks:
            self.tasks[task_name].append(new_duration)
            print(f"Updated task: {task_name} with new duration: {new_duration:.2f} seconds")
        else:
            print(f"Task {task_name} not found in timesheet.")
