# Encapsulation
# Abstraction
# some special naming convention
# name mangling

class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.__price = price

    def MakeCall(self,phoneNum):
        print(f"calling {phoneNum} ...")

    def fullName(self):
        return f"{self.brand} {self.model}"


Phone1 =Phone('nokia', '1100',1000)


# _name # convention of private name (In python all is public )

# __name__   #  dunder/magic method

# print(Phone1.__price)
# Phone1._price = -1000
# print(Phone1.__price)
print(Phone1.__dict__)

# name mangling ( _classname__instance Variable name  ) # python name change kar deta hai
print(Phone1._Phone__price)
Phone1._Phone__price = -1200
print(Phone1._Phone__price)





