# map function


# square of element


def sqr(a):
    return a**2

num = [2,3,4,5,6]

# using map function with function, return iterable map object , so convert it in list
square = list(map(sqr,num))
print(square)



#  using map function with lambda expression

square1 = list(map(lambda a: a**2,num))
print(square1)

# same problem using list comprehension
square2 = [i**2 for i in num]
print(square2)


# ...............................................................

name = ['abc','qwer','asd']
length = map(len,name)
for i in length:
    print(i)

# isase pta chlata hai ki map object me keval ek bar loop chalta hai
for j in length:
    print(j)

