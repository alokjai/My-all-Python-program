# enumerate function
# we use enumerate function with for loop to track positiion of our item in iterable


# how we  can do this without enumerrate function
names = ['abc', 'abcdf','qwert']
# 0 -- 'abc'
# 1 -- 'abcdf'
pos = 0
for name in names:
    print(f"{pos} ----> {name}")
    pos +=1


# ........................................
print()
# with  enumerate function
for pos, name in enumerate(names):
    print(f"{pos} ----> {name}")


# for example.................................
def func(lst1 , lst2):
    for pos, name in enumerate(lst1):
        if name == lst2:
          return pos
    return -1


names = ['abc', 'abcdf','qwert']

print(func(names,'abcf'))