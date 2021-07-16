# chapter 5 - list
# list is a data structure
# ordered collection of items
# you can store anything in lists int, float, string


# numbers = [1,2,3,4,5]
# print(numbers)

# words  = ["alok","all","ram","kam"]
# print(words)
# print(words[:2])

# mix  = [1,2,3,4,5,"alok","all","ram","kam"]
# print(mix)
# print(mix[-1])


# mix[4:7] = ["three","four"]
# print(mix)

# mix[1:] = "three"
# print(mix)

# how to add item to our list................................
# most common thing that you can do with your list and most important 

# append() - add item in last of list

fruits  = ["apple","pea","orange"]
fruits.append("banana")
print(fruits)  


# insert()- to insert data in list , where you want place.
fruits.insert(0,"grapes")
print(fruits)

# concatination two list using "+"
fruits2  = ["pineapple","tomato"]
# fruits3 = fruits + fruits2
# print(fruits3)

# concatination two list using extend()
fruits.extend(fruits2)
print(fruits)
print(fruits2)

print("diffrence append and extend........")
# diffrence between append and extend
fruits.extend(fruits2)
print(fruits)
fruits.append(fruits2) # it create list inside list
print(fruits)

# delete data from list...............
print("................delete data from list.......")
# using pop() method, by default delete last item in list  
fruits  = ["apple","pear","orange","banana","grapes"]
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)

# using del keyword

del fruits[0]
print(fruits)

# using remove()
fruits  = ["apple","pear","orange","apple","banana","grapes"]
fruits.remove("apple") # it delete first apple
print(fruits)


# checking  list that item is present or not...............
# print("........check list item presnt are not ...........")
# if "apple" in fruits:
#     print("apple is present ")
# else:
#     print("not present")    



# count()method
fruits  = ["apple","pear","orange","apple","banana","grapes"]
print(fruits.count("apple"))

# sort - sorted item in alphabetically

fruits.sort()
print(fruits)

number = [23,45,2,67,32,12]
number.sort()
print(number)

# when we want to print sorted item not store then use sorted()
number = [23,45,2,67,32,12]
print(sorted(number))
print(number)

number.sort()
print(number)

# clear()- clear list
number.clear()
print(number)

# copy() 
number = [23,45,2,67,32,12]
newNumber = number.copy()
print(newNumber)

# compare list 
# == , is
print("..........compare list .........")
print(number == newNumber) # check  value is same or not 
print(number is newNumber)  # check  memory place is same or not 


# split() method
# convert string to list
userInfo = "alok 23".split()
print(userInfo)

userInfo = "alok,26".split(',')
print(userInfo)



# join() method
# convert list to string
users = ["alka","swyam","34"] # don't use number either given error
print(','.join(users))
print(' '.join(users))



# list vs array

# list - store data any type
# array - store fix data type
# javascript array == python list

# list vs string
# string are immutable
# list are mutable

# looping in list
# for loop
fruits  = ["apple","pear","orange","apple","banana","grapes"]

# for frut in fruits:
#     print(frut) 

# while loop
# i=0
# while i < len(fruits):
#      print(fruits[i]) 
#      i+=1

#................////////............................
# list inside list
print()
print(".......list inside list.........")
matrix = [[1,2,3],[4,5,6],[7,8,9]]   #......2d list     
print(matrix[0])

for sublist in matrix:
    for i in sublist:
        print(i)
    print()

print(matrix[2][0])
print(type(matrix))