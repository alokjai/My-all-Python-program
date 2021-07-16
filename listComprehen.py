# list comprehension
# with the help of list comprehension we can create of list in one line

# list comprehension with for loop

#.........................................................
# create a list of square from 1 to 10
# square = []
# for i in range(1,11):
#     square.append(i**2)
# print(square)    

# by using list comprehnesion
# square2 = [i**2 for i in range(1,11)]
# print(square2)

# ........................................................
# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

# by using list comprehnesion

# newNegative = [-i for i in range(1,11)]
# print(newNegative)

# ........................................................

# name = ['alok','slok','mohan','sohan']
# newList = []
# for i in name:
#     newList.append(i[0])
# print(newList)    


# newList2 = [i[0] for i in name]
# print(newList2)


# list comprehension with if statement.......................

# numbers = list(range(1,11))
# num = []
# for i in numbers:
#     if i%2==0:
#         num.append(i)
# print(num)


# evenum = [i for i in numbers if i%2==0]
# print(evenum)



# list comprehension with if-else statement.......................

# nums = [1,2,3,4,5,6,7,8,9,10]
# newlst = []
# for i in nums:
#     if i%2 == 0:
#         newlst.append(i*2)
#     else:
#         newlst.append(-i)    

# print(newlst)

# # by using list comprehnesion
# newlst2 = [i*2 if (i%2 == 0) else -i for i in nums]
# print(newlst2)




# nested list comprehension............................

# example = [[1,2,3],[1,2,3],[1,2,3]]
newlst = []
for j in range(3):
    newlst.append([1,2,3])
print(newlst)


# by using list comprehnesion
nestedlst = [[i for i in range(1,4)] for i in range(3)] 
print(nestedlst)