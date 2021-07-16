


def func(*args,reveStr = False):
    namelst = []
    if reveStr == True:
        namelst = [l[::-1].title() for l in args]
        return namelst
    else:
        namelst = [k.title() for k in args]
        return namelst
    
name  = ['aok','rahul','ashish']
print(func(*name,reveStr=True))
# print(func(['aok','rahul','ashish'],reveStr=True)) # as you wish 


# same program use kwargs

def func2(lst,**kwargs):
    if kwargs.get('reveStr') == True:
        return [l[::-1].title() for l in lst]
    else:
        return [k.title() for k in lst]

name  = ['aok','rahul','ashish']
print(func2(name))        
    
