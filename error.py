# def add(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a+b
#     raise TypeError('oops you are passing wrong data type to function')

# print(add('2','8'))


# example (1),,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# raise errors 
# NotImplementedError
# abstract method


class Animal:
    def __init__(self,name):
        self.name = name


    def sound(self):
        #return "this is animal sound"
        raise NotImplementedError("you have to define this method in subclasses") #abstract method

class Dog(Animal):
    def __init__(self,name ,bread):
        super().__init__(name)
        self.bread = bread

    def sound(self):
        return 'bhau bhau'    

class Cat(Animal):
    def __init__(self,name ,bread):
        super().__init__(name)
        self.bread = bread
    def sound(self):
        return 'myau myau'

doggy = Dog('tia','any')
print(doggy.sound())


# example (2),,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


class Mobile:
    def __init__(self,name):
        self.name = name


class MobileStore:
    def __init__(self):
     self.mobiles = []

    def addMobile(self,newMobile):
        if isinstance(newMobile , Mobile):
            self.mobiles.append(newMobile)
        else:
            raise TypeError('new mobile should be object of mobile class')

oneplus = Mobile('one plus 6')
samsung = 'samsung galaxy s8'
mobostore = MobileStore()
# print(mobostore.mobiles)            
mobostore.addMobile(oneplus)
phone = mobostore.mobiles

print(phone[0].name)







