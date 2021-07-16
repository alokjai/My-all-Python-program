# define a function which will take list of word as a argument and 
# this function will return  list with reverse of every element in that list


# examople
# ['abc','tuy','xvz'] ------> ['cba','yut','zvx']


def reve(lst):
    reversVar = []
    for sublist in lst:
       reversVar.append(sublist[::-1])
    return reversVar

name = ["asd","qwe","zxc"]
print(reve(name))
