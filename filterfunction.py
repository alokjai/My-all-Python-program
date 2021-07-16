# filter function
# it return iterable filter object.only one time loop run 
# but convert into list or tuple you can more time loop run

# find even list 

def iseven(a):
   return a%2 == 0

num = [3,4,5,6,7,9,8,10]

evenlst = list(filter(iseven,num))
print(evenlst)



# using lambda expression
evenlst = tuple(filter(lambda a:a%2==0,num))
print(evenlst)
print()

for i in evenlst:
    print(i)

print()
for j in evenlst:
    print(j)

print()
for j in evenlst:
    print(j)
