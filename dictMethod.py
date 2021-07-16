# fromkeys() method
#  d = {'name':'unknown', 'age':'unknown'}

d = dict.fromkeys(['name','age'],['unknown'])
print(d)

d = dict.fromkeys(('name','age','state'),('unknown'))
print(d)

d = dict.fromkeys('abc','unknown')
print(d)

d = dict.fromkeys(range(1,11),'unknown')
print(d)


# clear() method .....................
# d.clear()
# print(d)

# copy() method.......................

# d1 = d.copy()
# print(d1.popitem())
# print(d)
# print(d1)


d1 = d
print(d1.popitem())
print(d)
print(d1)




# get method  (important)..................
d = {'name':'alok', 'age':'20'}
# print(d['names']) # jo key isme nahi hai yadi usko print karaye to yah error dega

print(d.get('names')) # yah nahi dega . yah 'none' return karega 
print(d.get('name'))

#if 'name' in userInfo:
#     print("present")
# else:
#     print("not present")

#if d.get('name'):
#     print("present")
# else:
#     print("not present")


# more about get(), when two same keys in dictionary
# user = {'name':'alok', 'age':20 ,'age': 34} # same keys are override 
# print(user)

# when we want to not return 'none' 
# print(user.get('fav','not found!')) 

