# generate lists with range function
# something more about pop method 
# index method
# pass list to a funtion
# min and max function

numbers = list(range(1,11))
print(numbers)

# numbers.pop()
# print(numbers)

# pop method also return a value  
print(numbers.pop())


# to find item's postion in list .return index no
# syntax:- index(value, start, stop)
print(numbers.index(4))
print(numbers.index(7,6))
print(numbers.index(7,6,8))



def negetiveList(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negetiveList(numbers))

print()
print("min and max.....")
# min and max ..............

number = [3,5,7,45]

print(min(number))
print(max(number))