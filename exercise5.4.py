# filter odd even
# define a function
# input
# list --- > [1,2,3,4,5,6,7]
# output ----> [[1,3,5,7],[2,4,6]]


def filterOddE(lst):
    filter = []
    odd = []
    even = []
    for l in lst:
        if l%2 == 0:
            even.append(l)
        else:
            odd.append(l)
    filter.append(even) 
    filter.append(odd)       
    return  filter          


num = [23,22,45,43,66,12,6,2]
print(filterOddE(num))