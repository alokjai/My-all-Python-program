# define a function which will take list as a argument and this function will return a reversed list

# note:- try to do this with the help of append and return method not reverse() or [::-1]
    
def rvrs(lst):
    rev = [] 
    for l in range(1,len(lst)+1):
     # rev.append(lst.pop())    
     poped = lst.pop()
     rev.append(poped)
    return rev    

number = [1,2,3,4,5]

print(rvrs(number))