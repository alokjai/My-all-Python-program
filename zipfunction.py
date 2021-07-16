# Zip function 
# it return iterater zip object,


userId = ['user1','user2', 'user3']
names = ['amar', 'anuj','sagar']
last = ['jaiswal','gupta','yadav']
# Zip function create like ('user1','amar'),('user2','anuj'),('user3','sagar') tuple

print(dict(zip(userId,names)))  # it convert dictionary

print(zip(userId,names))

print(list(zip(userId,names)))

print(tuple(zip(userId,names)))

print(tuple(zip(userId,names,last)))
# print(dict(zip(userId,names,last)))  # it gives error 

# /............................................................................


# l1 = [1,3,5,7]
# l2 = [2,4,6,8]

l = [(1,2),(3,4),(5,6),(7,8)]  # output
# * operator with zip

print(list(zip(*l)))


l1, l2 = list(zip(*l))
print(l1)
print(l2)

# ............................................
print()
# check greater in pair
l1 = [1,3,5,7]
l2 = [2,4,6,8]
newlst = []
for pair in zip(l1,l2):
    newlst.append(max(pair))

print(newlst)



# practice ........................................
print()
print()
def avg(l1,l2):
    new = []
    for pair in zip(l1,l2):      
        av1 = sum(pair)/len(pair)
        new.append(av1)
    return new    
        
l3 = [1,3,5,7]
l4 = [2,4,6,8]       
print(avg(l3,l4))   
       
#  using *args 

print()
print()
def avg2(*args):
    new = []
    for pair in zip(*args):      
        av1 = sum(pair)/len(pair)
        new.append(av1)
    return new    
        
l3 = [1,3,5,7]
l4 = [2,4,6,8] 
l5 = [5,6,3,8]      
print(avg2(l3,l4,l5))




#  using lambda expression

avgfind = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]

print(avgfind([1,3,5,7],[2,4,6,8]))