class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.acc = True
        self.clutch = True
        print("Car start....")
    
    def stop(self):
        self.acc = False
        self.clutch = False
        self.brk = True
        print("Car stop...")

s1 = Car()
s1.start()
s1.stop()