# example
# number = [1,2,3,4]
# squarelist(number) .....>return ------>[1,4,9,16]


def listsquar(lst):
    sqr = []
    for l in lst:
      sqr.append(l**2)
    return sqr


number = [1,2,3,4]
print(listsquar(number))