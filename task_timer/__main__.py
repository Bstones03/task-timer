"""
task.py  (__main__.py file)
Brennen Stones <brennen.stones@student.cune.edu>
<The date in YYYY-MM-DD format>
 
<Short Description>
"""

import click
from task_timr import TaskTimer 


@click.command()
def main():
    timer = TaskTimer()
    while True:
        print("\nOptions: start, stop, summary, current, export, edit, exit")
        choice = input("Select an option: ").strip().lower()
        
        if choice == 'start':
            task_name = input("Enter task name: ")
            timer.start_task(task_name)
        elif choice == 'stop':
            timer.stop_task()
        elif choice == 'summary':
            timer.print_timesheet()
        elif choice == 'current':
            timer.current_running_task()
        elif choice == 'export':
            filename = input("Enter filename (default: timesheet.csv): ") or 'timesheet.csv'
            timer.export_timesheet(filename)
        elif choice == 'edit':
            task_name = input("Enter task name to edit: ")
            new_duration = float(input("Enter new duration (seconds): "))
            timer.edit_timesheet(task_name, new_duration)
        elif choice == 'exit':
            print("Exiting the task timer.")
            break
        else:
            print("Invalid option. Please try again.")
        

        


if __name__ == '__main__':
    main() 