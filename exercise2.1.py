# x , y , z = int(input("Enter 3 number").split())
x = int(input("first number "))
y = int(input("second number "))
z = int(input(" third number"))
avg = (x+y+z)/3
print("average is {}".format(str(avg)))


# ...........one line input.....

x , y , z = input("Enter 3 number").split()
avg = (int(x)+int(y)+ int(z))/3
print(f"average is {avg}")

# exercise 2.............
name = input("enter your name ")
print(f"reverse name is {name[-1::-1]}")