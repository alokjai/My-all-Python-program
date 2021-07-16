def greater(a,b):
    if a > b:
        return a  #(f"{a} is greater")
    return  b    #(f"{b} is greater")

print(greater(3,4))

def greater1(a,b,c):
    if a>b:
        return f"{a} is greater"
    if b>c: 
         return f"{b} is greater"   
    return f"{c} is greater"

print(greater1(4,10,9))

# function inside function

# def Newgreater(a,b,c):
#    bigger = greater(a,b)
#    return greater(bigger,c)

# kiss = keep it simple stupid
def Newgreater(a,b,c):
   return greater(greater(a,b),c)

print(Newgreater(24,35,45))   