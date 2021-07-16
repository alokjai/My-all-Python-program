class Person:
    Count = 0
    def __init__(self,firstname,lastname,age):  
        self.first = firstname
        self.last = lastname
        self.age = age
        Person.Count += 1

    def fullName(self):
        return f"{self.first} {self.last}"    

    def isAbove(self):
        return self.age > 18


p1 = Person('alok','jaiswal',20)
p2 = Person('ram', 'gupta',23) 

print(Person.Count)