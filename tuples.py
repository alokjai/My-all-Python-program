# tuple is data structure
# tuple can store any data type 
# kost impotant tuples are immutable, once tupke is created you can't update
# data inside tuple.

# Example = ("one","two","three")
# no append , no insert , no pop , no remove
# tuple are faster than lists

# method
# count, Index
# len function
# slicing

# .................................................................................................................

# looping in tuple
mix = (1,2,3,4.23)

for l in mix:
    print(l)
# you can use while loop too
    
# tuple with one element
# one element is not tuple but one element with comma(',') are tuple
num = (1)
num1 = (1,)
words = ('one')
print(type(num))
print(type(num1))
print(type(words)) 

print()
# tuple without paranthesis ()
name = "alok","aman","sagar","amar"
print(type(name))

print()
# tuple unpacking
name = ("alok","aman","sagar","amar")
name1, name2, name3,name4 = (name)
# number of variable == number of element in tuple must be equal otherwise get error 
print(name1)
print(name2)
print(name3)

# list inside tuple
# in list we can update data
fruits = ("apple",["banana","pear"])
fruits[1].pop()
print(fruits)

fruits[1].append("lichi")
print(fruits)


# some function min, max , sum

print(min(mix))
print(max(mix))
print(sum(mix))


# function returning two values.............
# function return a tuple, we can store value in diffrent vaiable.
print()
print("function returning two values............. ")

def func(num1,num2):
    add = num1 +num2
    multyply = num1*num2
    return add , multyply

tup = func(2,3)
print(tup)
print(type(tup))  # only return a tuple

a,b = func(3,4)
print(a)
print(b) 

# something more about tuple,list,str
nums = tuple(range(1,11))
print(nums)

# to convert tuple to list
num = list((1,2,3,4,5,6,7))
print(type(num))


# to convert tuple to string
num = str((1,2,3,4,5,6,7))
print(type(num))


