# class variable
# circle class
# method  : area , circum


class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def circum(self):
        return 2*Circle.pi*self.radius


c = Circle(5)
c1 = Circle(8)

print(c.circum())

# class method ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,..,,,,,,,,,,,,,.,.

# class Person:
#     Count = 0
#     def __init__(self,firstname,lastname,age): 
    
#         self.first = firstname
#         self.last = lastname
#         self.age = age
#         Person.Count += 1

#     @classmethod
#     def CountInsta(cls):
#         return f"You have created {cls.Count} instances of {cls.__name__} class"


#     def fullName(self):
#         return f"{self.first} {self.last}"    

#     def isAbove(self):
#         return self.age > 18


# p1 = Person('alok','jaiswal',20)
# p2 = Person('ram', 'gupta',23)  

# print(Person.CountInsta())


# class method as constructor(how to make object without init method)

class Person:
    Count = 0
    def __init__(self,firstname,lastname,age): 
    
        self.first = firstname
        self.last = lastname
        self.age = age
        Person.Count += 1

    @classmethod
    def CountInsta(cls):
        return f"You have created {cls.Count} instances of {cls.__name__} class"
    
    @classmethod  #  ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    def CreateObj(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)

    
    @staticmethod
    def hello():
        print("hello static method")

    def fullName(self):
        return f"{self.first} {self.last}"    

    def isAbove(self):
        return self.age > 18




p1 = Person.CreateObj("Amar,gupta,24")
print(p1.fullName())
print(p1.last)

# static method call
Person.hello()
