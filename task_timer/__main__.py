"""
__main__.py for task_timer
Brennen Stones <brennen.stones@student.cune.edu>
2025-02-06
 
This is the main user I/O for the task timer
It's connected to the task_timr.py and it's corresponding class
the U/I just gives the user all the options and takes in a string
this string either will correspond to an option or request a new response
it will loop infinitely unless exited or ctrl+C
"""

import click
from task_timr import TaskTimer 


@click.command()
def main():
    """user I/O and menu"""
    timer = TaskTimer()
    while True:
        #loop for user I/O
        print("\nOptions: start, stop, summary, current, export, edit, exit")
        choice = input("Select an option: ").strip().lower()
        
        if choice == 'start':
            #start selection
            task_name = input("Enter task name: ")
            timer.start_task(task_name)
        elif choice == 'stop':
            #end current task
            timer.stop_task()
        elif choice == 'summary':
            #prints out all tasks run and ended with time
            timer.print_timesheet()
        elif choice == 'current':
            #print out snapshot of running task with time
            timer.current_running_task()
        elif choice == 'export':
            #export report of all run tasks and times as csv file
            filename = input("Enter filename (default: timesheet.csv): ") or 'timesheet.csv'
            timer.export_timesheet(filename)
        elif choice == 'edit':
            #change time recorded for task
            task_name = input("Enter task name to edit: ")
            new_duration = float(input("Enter new duration (seconds): "))
            timer.edit_timesheet(task_name, new_duration)
        elif choice == 'exit':
            #exit program
            print("Exiting the task timer.")
            break
        else:
            #error with selection
            print("Invalid option. Please try again.")
        

        


if __name__ == '__main__':
    main() 