import time
import threading
from datetime import datetime,timedelta
class CountdownTimer:
    def __init__(self, start_time=120):
        self.start_time = start_time
        self.current_time = start_time
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.run)
            self.thread.daemon = True 
            self.thread.start()

    def run(self):
        while self.running:
            for i in range(self.start_time, -1, -1):
                if self.current_time == 120:  
                    self.current = datetime.now()
                    self.end = datetime.now()+timedelta(minutes=2)
                self.current_time = i
                time.sleep(1)
                print(self.current_time)
                if not self.running:
                    break
            self.current_time = self.start_time

    def stop(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()

    def get_current_time(self):
        return self.current_time
    def starting(self):
        return self.current
    def ending(self):
        return self.end

timer = CountdownTimer()