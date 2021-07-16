# set is data type
# unoredered collection of unique items
# store any data type 
# you can not store list or dictionary in set
s = {1,2,3,2,1}
print(s)
print(type(s))

# print(s[1]) # error

lst = [1,2,3,4,4,3,3,7,2,1,6,8]
# remove duplicate
# convert list to set using set()........important
s2  = set(lst)
print(s2)

# convert set to list using list() .......important
s3  = list(s2)
print(s3)


# add element in set
s.add(4)
print(s)
s.add(4)
print(s)

# remove element into set
s.remove(4)
print(s)

# s.remove(5) # error
# print(s)

# s.discard(5) # not error because 5 does not exist 
# print(s)

# s.clear()
# print(s)

s1 = s.copy()
print(s1)



# in keyword in sets and for loop

s = {'a','b','c'}

if 'a' in s:
    print("present")
else:
    print("not present")

for i in s:
    print(i)  


# sets Maths
s1 = {1,2,3,4,5}
s2 = {3,4,5,7,6}     
# for union using pipe ('|')
union = s1 | s2
print(union)

# for intersection using '&'
intrsec = s1 & s2
print(intrsec)