import time

class Stopwatch: 
    def __init__(self):
        self.start_time = None
        self.elapsed = 0
        self.running = False

    def start(self):
        self.start_time = time.time()
        self.running = True
    
    def pause(self):
        self.elapsed = time.time() - self.start_time
        self.running = False
    
    def reset(self):
        self.start_time = None
        self.elapsed = 0
        self.running = False


    def get_time(self):
        if self.running:
            return time.time() - self.start_time
        return self.elapsed
