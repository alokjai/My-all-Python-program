# list comprehension
# define a functiom that take list of strings
# list containing reverse of every strings

def reve(lst):
    newlst = [l[::-1] for l in lst]
    return newlst    

lst1 = ['asd','zxc','qwe','dfg']
print(reve(lst1))    