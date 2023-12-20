name = "Nhan"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_two = greeting.format("Han")

print(with_name)
print(with_name_two)

###################################################

#namsinh = int(input("Nhap vao nam sinh: "))
#tuoi= 2023 - namsinh
#print(f"Tuoi cua ban la {tuoi}")

###################################################

l=["A", "B", "C"]
t=("A", "B", "C")
s={"A", "B", "C"}
k={"A", "D", "C"}

l.append("D")
s.add("E")
print(s)

both= s.intersection(k)
print(both)

friends= ["R","B"]
abroad= friends

print(friends == abroad)
print(friends is abroad)
print("B" in friends)

Str= "AbCD"
str= Str.lower()
print(str)

grades = [9, 10, 6, 8]
total=0
for grade in grades:
    total= total + grade

print(total)

bans= ["Anh", "Cam", "Bao"]
starts_s=[]

for ban in bans:
    if ban.startswith("B"):
        starts_s.append(ban)

print(starts_s)

student_attendance = {"Rolf": 96, "Bob":80, "Anne":100}

for student in student_attendance:
    print(f"{student}:{student_attendance[student]}")

people = [("Bob", 42, "Mechanic"),("Jame", 24, "Artist")]

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

(lambda x, y: x + y)(5,7)

class Student:
    def __init__(self, name, grades):
        self.name= name
        self.grades= grades

    def average_grade(self):
        return sum(self.grades)/len(self.grades)
    
student = Student("Bob")
print(student.name)
print(student.average_grade())