class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)

    def __str__(self):
        return f"Person {self.name}, {self.age} years old."
    
    def __repr__(self):
        return f"Person {self.name}, {self.age} years old."
    
bob = Person("Bob",22)
print(bob)

