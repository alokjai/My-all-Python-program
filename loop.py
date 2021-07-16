i=1
while i<=10:
    print("hello world \n")
    i = i + 1

# sum: 1 to 10 
k=1
sum = 0
while k<=10:
    sum =sum + k # sum += k
    k = k +1
print(sum)

# for loop  

#for i in range(10):  # 0 to 9
#    print("hello world")

#for i in range(1 ,10):  # 1 to 9
#    print("hello world")    

for i in range(1 , 11):  # 1 to 10
    sum += i
print(sum)

# break statement
for i in range(1 , 11):  # 1 to 10
    if i == 5:
     break
    print(i)

# continue statement
for i in range(1 , 11):  # 1 to 10
    if i == 5:
     continue
    print(i)

# step argument 
for i in range(1,10,2): # two number gap in loop. this 2 is step argument 
    print(i)

for i in range(11,0,-1):
    print(i)

for i in range(0,-11,-1):
    print(i)

# for loop with string

name = "alok"
for i in name:
    print(i)


# problem
# ask user  to input  a number  containing  more  than one digit
# example : 1231
# calculate 1+2+3+1 and print

num = input("enter number ")
sum = 0
for i in num:
    sum += int(i)
print(sum)    