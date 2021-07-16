# * operator
# *args
# make flexible function

# def total(a,b):
#     return a+b

# print(total(3,6,7,4)) # error

# def all(*args):  # yahan args sirf naam yah koi keyword nahi hai. aap change bhi kar sakte ho 
#    print(args)   # yah tuple form me input leta hai 
#    print(type(args))

# all(1,2,3,4,5,6)   


def allTotal(*args):
    total = 0
    for num in args:
        total += num
    return total    

print(allTotal(2,4,5,3,6))


print()

# *args with normal parameter..............................

def multiply(num,*args): # normal parameter me *args hamesha last me pass kiya jata hai . otherwise error
    mul = 1
    print(num)
    for i in args:
        mul *= i
    return mul

print(multiply(2,3,4))


# *args as argument................................
# yadi function call karte samay list pass kare to, for exa,ple multiply me 1 ek list se guna karega 
# jo sahi nahi hai , isliye *args as a argument passs karte hai jo list ko unpack kar deta hai
print()
def multiply2(*args): 
    mul = 1
    print(args)
    for i in args:
        mul *= i
    return mul

num = [2,3,4]
print(multiply2(*num))  # unpack num



print()

# kwargs (keyword arguments)
# **kwargs (double star operator)

# kwargs as a parameter
# ya
# yah key : value ke form me input leta hai , dictionary me store karta hai
def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} :{v}")
    print(kwargs) # as you wish print 
    print(type(kwargs))

func(first = 'alok',last = 'jaiswal')


print()
# **kwargs with normal parameter..............................

def func2(name,**kwargs):
    for k, v in kwargs.items():
        print(f"{k} :{v}")
   

func2('amit',first = 'alok',last = 'jaiswal')




# dictionary unpacking ..........................................
print()
def func3(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} :{v}")

d = {'name':'alok','age' : 23}
func3(**d)



# function with all parameter 
# very important..

# use all parameter type , it means default ,*args , normal ,**kwargs parameter
# oreder is :- normal, *args, default, **kwargs
# for remember --- PADK(parameter,args,default,kwargs)
# keep maintain order
def func4(name,*args,lastName = "unknown",**kwargs):
    print(name)
    print(args)
    print(lastName)
    print(kwargs)

func4('samar',23,45,6, 'gupta',fruit = 'apple',price = 50)




