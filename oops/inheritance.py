class Car:
    @staticmethod
    def start():
        print("Car start...")
    
    def stop():
        print("Car stop...")

class TataCar(Car):
    def __init__(self,name):
        self.name = name
        print(self.name,"is ")

car1 = TataCar("Tata Safari")
car1.start()

        