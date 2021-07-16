# any , all function
num1 = [2,4,6,5,10]
num2 = [1,3,5,7,9]

even1 = []
for num in num1:
    even1.append(num%2 == 0)

print(even1)



print(all([True, True, True, True, True])) # all() jab uske saare element true ho to true return karta hai nahi to false


# using list comprehension
print(all([num%2 == 0 for num in num1]))



print(any([num%2 == 0 for num in num2])) # any() yadi ek bhi element condition ko satisfy karta hai to true return karta hai







# practice .  ...............................  ........................

print()
print()
def add(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for num in args:
            total +=num
        return total
    else:
        return "wrong input"


print(add(1,2,3,4,5,6,'alok',['samar']))

print(add(1,2,3,4,5,6))


