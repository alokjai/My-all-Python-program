# Generator are iterators

# l = [1,2,3]    # ....iterable

# square  = [a**2 for a in l]  
# square is iterators

# type to create Generator
# 1) generator function                    # 2) generator comprehension

# 1)generator function

def num(n):
    for i in range(1,n+1):
        yield i  #  this is a keyword mot function to create generator


# print(num(8)) # it generator object

numbers = num(10)

for numb in numbers:
    print(numb)

for numb1 in numbers:
    print(numb1)

# yahan par dobara looop nahi chalega kyunki memory empty hai



# 2) generator comprehension..........................................
print()
# same as list comprehension use paranthesis() not []
square = (i**2 for i in range(1,11))
print(square)

for num in square:
    print(num)



# list vs generator...........,,,,,,,,,,,..,,.,,.,,................,,,,,,,,,,,,,,,,


# l = [i**2 for i in range(1000000)]

l = (i**2 for i in range(1000000))


import time

t1 = time.time()
l = [i**2 for i in range(1000000)]
t2 = time.time()
print(t2-t1)



t1 = time.time()
l = (i**2 for i in range(1000000))
t2 = time.time()
print(t2-t1)



