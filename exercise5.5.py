# common element finder functiion
# define a functiion which take 2 lists as input and return a lists
# which contains common elements of both lists

# example
# input ---> [1,2,3,4], [1,2,6,7]
# output --> [1,2]

def common(lst1,lst2):
    temp = []
    for l in lst2:
        if l in lst1:
          temp.append(l)
    return temp

num1 = [2,3,5,6,4,7]
num2 = [6,8,9,2,9,3,7,5]

print(common(num1,num2))
