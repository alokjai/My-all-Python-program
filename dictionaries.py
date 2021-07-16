# dictionaries is unordered collection of data in key : value pair.

# Q - why we use dictionaries ?
# A - because of limitation of lists, list are not enough to represent real data.

# Example :-
# user = ['harshit', 23, ['coco', 'kimino na wa'],[''awaking', 'fairy tale']]
# this lists contains user name, age , fav movies , fav tunes
# you can do this but this is not a good way to do this.

# how to create dictionaries
user = {'name' : 'alok', 'age':'20'}
# print(user)
# print(type(user))


# second method to create dictionaries
# user = dict(name = 'alok', age = '20')
# print(user)
# print(type(user))


# how to access data from dictionaries
#Note :- There is no indexing because of unordered collection of data.
# print(user[0])  # error--

print(user['name'])
print(user['age'])


# which type data a dictionaries can store ?
# anytype of data

userInfo = {
    'name' : 'alok',
    'age' : 20,
    'rollno' : 17,
    'favtune' : ['awaking', 'fairy tale']
}

print(userInfo)
print(userInfo['favtune'])


# how to add data  to empty dictionary

users = {}
users['name'] = 'mohit'
print(users)

# in keyword and iteration in dictionary............................

# check if key exist in dictonary
# if 'name' in userInfo:
#     print("present")
# else:
#     print("not present")    


# check if value exist in dictonary  ......values method  
# if 'alok' in userInfo.values():
#          print("present")
# else:
#      print("not present")


# loops in dictionary

# for i in userInfo: # it print only key
#     print(i)

# for i in userInfo.values(): # it print only value
#     print(i)    

for i in userInfo:
    print(userInfo[i])

# values method 
# users = userInfo.values()
# print(users)
# print(type(users))


# items method ......(important)
users = userInfo.items() # it return tuple
print(users)
print(type(users))


# for key, value in userInfo.items():
#     print(f"Key is {key} and value is {value}")



# add and delete data

userInfo1 = {
    'name' : 'slok',
    'age' : 23,
    'rollno' : 43,
    'favtune' : ['awaking', 'fairy tale']
}    

# userInfo1['favSong'] = ['song1','song2']
# print(userInfo1)

# pop method

# popItem = userInfo1.pop('favtune') # is wale pop() argument pass karna hi hoga nahi to error aayegi
# print(popItem) # yah jis prakar ka datatype hoga usi datatype formate me return karega
# print(userInfo1)


# popitem method

# poppedItem = userInfo1.popitem() 
# print(poppedItem) # it return tuple
# print(userInfo1)



# update dictionary
moreInfo = {'name' : 'alok jaiswal' , 'state' : 'up'}
userInfo1.update(moreInfo)
print(userInfo1)
userInfo1.update({}) # no delete any data. it means no updation
print(userInfo1)





# yadi kisi list me tuples hai aur har tuple me two value hai to use dictionary me change kar sakte hai

example = [('a',2),('b',4)]
print(dict(example))
