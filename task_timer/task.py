"""
task.py
Brennen Stones <brennen.stones@student.cune.edu>
<The date in YYYY-MM-DD format>
 
<Short Description>
"""

import datetime


class Task:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = datetime.now()

    def stop(self):
        self.end_time = datetime.now()

    def duration(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return None