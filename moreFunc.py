# what is doc strings.....................................................
# we use triple single quotes ('''   ''') or triple double quote ("""   """)
# doc string msg hota hai jo user ko aapke function ke baare me batane ke liye use hota hai

def add(a,b):
    ''' this function tkes 2 numbers and return their sum '''
    return a+b

print(add(2,3))
print(add.__doc__)

# print(len.__doc__)
# print(sum.__doc__)
# print(max.__doc__)


print()
print()

# help function .........................................
# print(help(add))
print(help(max))





