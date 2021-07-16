# create class 
# init method or constructer
# atribute and instance variable
# create object

# self ko aap yahan kuch bhi name de sakte hai but uska use har attribute me karna hoga

class Person:
    def __init__(self,firstname,lastname,age):  # these are attribute
        print("init method / constructer call")
         #instance variable
        self.first = firstname
        self.last = lastname
        self.age = age

    def fullName(self):
        return f"{self.first} {self.last}"    

    def isAbove(self):
        return self.age > 18


# create object
p1 = Person('alok','jaiswal',20)
p2 = Person('ram', 'gupta',23)    

print(p1.first)
print(p2.first)
print(p2.fullName())
print(p1.isAbove())
# same as 
# print(Person.fullName(p2))









