# sum of n natural nrmbers
# ask a user for natural numbe(n)
# print total from 1 to n

num = int(input("enter number to sum "))
i = 1
sum = 0
while i<=num:
    sum += i
    i +=1
print(sum)