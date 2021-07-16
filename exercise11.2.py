



# class Laptop:
#     def __init__(self,brand, modelname,price):
#         self.brand = brand 
#         self.model = modelname
#         self.price = price

#     def applyDis(self,num):
#        dis = self.price - self.price * num/100
#        return dis



# l1 = Laptop('dell','vostro',380000)
# l2 = Laptop('hp','notebook',400000)


# print(l1.brand)
# print(l1.model)

# print(l1.applyDis(40))




# .,,,,,,,,,....,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

class Laptop:
    discount = 10
    def __init__(self,brand, modelname,price):
        self.brand = brand 
        self.model = modelname
        self.price = price

    def applyDis(self):
       dis = self.price - self.price * self.discount/100
       return dis



l1 = Laptop('dell','vostro',380000)
l2 = Laptop('hp','notebook',400000)


print(l1.__dict__)
l1.discount = 50
print(l1.__dict__)
print(l1.price)



