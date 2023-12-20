class Student:
    def __init__(self, name, grades):
        self.name = str(name)
        self.grades = tuple(grades)
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    
student = Student("Bob",(10,5,7,8))

print(student.name)
print(student.average_grade())