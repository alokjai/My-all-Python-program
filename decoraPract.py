# define a decorator function 
# calling -- print(add(a,b)) 
# output:-
# you are calling add function
# This function takes two numbers as argument and return their sum
# sum



# from functools import wraps
# def Printdata(anyfunc):
#     @wraps(anyfunc)
#     def wrapper(*args,**kwargs):
#         print(f"you are calling {anyfunc.__name__}")
#         print(anyfunc.__doc__)

#         return anyfunc(*args,**kwargs)
#     return wrapper

# @Printdata
# def add(a,b):
#     '''This function takes two numbers as argument and return their sum '''
#     return a+b

# print(add(2,3))    



#   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,next problem ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


# only int allow
from functools import wraps
def onlyint(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        if all([type(arg) == int for arg in args]):
            return function(*args,**kwargs)
        print("please enter integer value not list or tuple")    
        # datatype = []
        # for arg in args:
        #     datatype.append(type(arg) ==int)
        # if all(datatype):
        #     return function(*args,**kwargs)
        # else:
        #       print("please enter integer value not list or tuple")             
    return wrapper
    

@onlyint
def add(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add(1,2,3,4))















