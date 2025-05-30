class Student:
    name = "Avinash"
    def __init__(self, fullName):
        self.name = fullName
        print("Hello",self.name)

s1 = Student("Avinash")
# print(s1)