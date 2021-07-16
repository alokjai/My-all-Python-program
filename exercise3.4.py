# problem
# ask user  to input  a number  containing  more  than one digit
# example : 1231
# calculate 1+2+3+1 and print

num = input("enter number more than 1 digit ")
i=0
sum = 0
while i<len(num):
   sum = sum + int(num[i]) 
   i = i+1
print(sum)   