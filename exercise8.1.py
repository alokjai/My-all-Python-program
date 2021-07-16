
def power(n,*args):
    if args:
       return [i**n  for i in args ]
    else:
        return "hey you didn't pass args"   

nums = [2,3,4,5]
print(power(2,*nums))
print(power(3))

print(power(2,*[5,7]))