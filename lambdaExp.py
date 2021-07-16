# lambda expresion (anonymous function)

# def add(a,b):
#     return a+b



add2 = lambda a,b : a+b
print(add2(2,3))

# uses of lambda in built-in,map , reduce, filter function

# mul = lambda a,b : a*b

# print(mul(2,3))



# lambda expresion (anonymous function) practice............


# def Even(a):
#     if a%2 ==0:
#         return True
#     else:
#         return False    
        
# def Even(a):
#     return a%2==0

# isEven  = lambda a : a%2 == 0
# print(isEven(5))

# .....................................
# def lChar(s):
#     return s[-1]


# lastchr = lambda a : a[-1]

# print(lastchr('alok'))

# ...............................
# lambda with if-else

def func(s):
    if len(s) > 5:
        return True
    return False

def func1(s):
    return len(s) > 5
        

func2 = lambda s : True if len(s) > 5 else False    
func3 = lambda s : len(s) > 5    
print(func3('alokit'))
