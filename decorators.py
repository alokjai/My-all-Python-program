# you have to a complete understanding of functions.
# first class  function / clousers 
# then finally we will learn abbout decoraters
   
def sqr(a):
    return a**2


s = sqr
print(s(3))


# memory location is same
print(s)
print(sqr)
# ...............................
print(s.__name__)
print(sqr.__name__)



# pass function as argument.............................
# for example

# l = [1,2,3,4]
# print(list(map(sqr,l)))
# print()
# print(list(map(lambda a : a**2 ,l)))

# ..........like a map functioon.....................

def mymap(func,l):
    newlst = []
    for item in l:
       newlst.append(func(item))
    return newlst

print()
l = [1,2,3,4]
print(mymap(sqr,l))



# .........function returning function ..........................

def outer():
    def inner():
        print("inside inner func")
    return inner  # ye execute nahi krega 

var = outer()
print(var())



def outer1():
    def inner():
        print("inside inner func")
    return inner()  # ye execute hoga

var = outer1()


# ................   ...............Clouser.................. ........
# function returning function (clousers) practice
print()
print()

def toPower(x):   
    def calcPower(n):
        return n**x
    return calcPower    

cube = toPower(3)
print(cube(2))

sqrrr = toPower(2)
print(sqrrr(3))






