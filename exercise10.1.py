# define generator function
# take one number as argument
# generator a sequence of even numbers from 1 to that number

def geneven(a):
    for l in range(1,a+1):
        if l%2 == 0:
            yield l

even = geneven(16)            
         
for l in even:
    print(l)











