# num to string
# define a function

# example 
# input -----> [True,False,[1,2,3],1,1.2,3]
# output ----> ['1','1.2','3']

def func(lst):
    newlst = [str(l) for l in lst if type(l) == int or type(l) == float]
    return newlst   

num = [True,False,[1,2,3],1,1.2,3]    
print(func(num))