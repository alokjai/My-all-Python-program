# Decorators - enhance the functionality of other function
# @ use for decorator (syntactic sugar)

def decorFunc(anyfunc):
    def wrapper():
        print("this is awesome function")
        anyfunc()
    return wrapper    


# this is awesome function
@decorFunc   # this is sortcut ..........
def func1():
    print('this is function 1')

# call 
func1()



# this is awesome function
def func2():
    print('this is function 2')


# var = decorFunc(func2)
# var()

#............................
# @decorFunc
# def func3(a):
#     print('this is function 3 with argument')

# func3('alok')    # this is error 'wrapper() takes 0 positional arguments but 1 was given'




# ..........................................................................

def decorFunc1(anyfunc):
    def wrapper(*args,**kwargs):
        print("this is 2nd awesome function")
        return anyfunc(*args,**kwargs)
    return wrapper 


@decorFunc1
def func3(a):
     print('this is function 3 with argument')

func3('alok')

print()

@decorFunc1
def add(a,b):
    return a+b

print(add(3,5))


# ..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..........................................

# from functools import wraps
def decorFunc2(anyfunc):
   # @wraps(anyfunc) # include
    def wrapper(*args,**kwargs):
        ''' this is wrapper function '''
        print("this is 2nd awesome function")
        return anyfunc(*args,**kwargs)
    return wrapper 

@decorFunc2
def add2(a,b):
    ''' this is add function '''
    return a+b

# when we print their doc string
print(add2.__doc__)
print(add2.__name__)
# output is :  
# this is wrapper function
# wrapper

# becouse we indirectly we call wrapper function not add()

# iss problem ko solve karne ke liye module import karna hoga

# from functools import wraps
# iske bad built in @wraps decorator ko call karna hoga



