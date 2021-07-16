# create a laptop class with attribute like name, modelname, price
# craete two object of your laptop class

class Laptop:
    def __init__(self,name, modelname,price):
        self.name = name 
        self.model = modelname
        self.price = price



l1 = Laptop('dell','vostro',380000)
l2 = Laptop('hp','notebook',400000)


print(l1.name)
print(l1.model)




