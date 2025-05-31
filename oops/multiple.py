# ...existing code...
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
        
class Electric:
    def charge(self):
        print("Charging electric vehicle...")

class ElectricTataCar(TataCar, Electric):
    def __init__(self, name):
        super().__init__(name)
        print(self.name, "is an electric Tata car.")

# Example usage:
electric_car = ElectricTataCar("Tata Nexon EV")
electric_car.start()
electric_car.charge()
# ...existing code...