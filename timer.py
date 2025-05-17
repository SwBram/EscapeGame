from component import Component
from datetime import datetime

class Timer(Component):
    def __init__(self, max_time: int):
        self.max_time = max_time
        self.start_time = None
        self.stop_time = None
        

    def startTime(self):
        self.start_time = datetime.now()

    def getDuration(self):
        return int((datetime.now() - self.start_time).total_seconds()) if self.start_time else 0

    def getRemaining(self):
        return max(0, self.max_time - self.getDuration())
    
    def stopTime(self):
        self.stop_time = datetime.now()