class Student:
    collage_name = "KIT"    #class attr
    def __init__(self, name):
        self.name = name    #instance attr
    
    def hello(self):
        print("hello", self.name)
        
obj = Student("Avinash Chaurasiya")
print(obj.name)
print(obj.collage_name)
obj.hello()
