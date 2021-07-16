# property and setter decorator
# property == getter()
# property decorator define karne ke bad hi setter decorator define kare 


class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self._price = max(price,0)
       # self.compSpeci = f"{self.brand} {self.model} and {self.price}"


    @property
    def compSpeci(self):
        return f"{self.brand} {self.model} and {self._price}"    
    
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,newprice):
        self._price = max(newprice,0)

    def MakeCall(self,phoneNum):
        print(f"calling {phoneNum} ...")

    def fullName(self):
        return f"{self.brand} {self.model}"


Phone1 =Phone('nokia', '1100',1000)
print(Phone1.price)
print(Phone1.compSpeci)



