class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hii", self.name, "your marks avarage is :",sum/len(self.marks))
    
s1 = Student("Avinash Chaurasiya", [90, 90, 90, 99, 100, 50])
s1.get_avg()