first = "alok"
last  = "pal"
full = first + last
print(full)
# error
# print(full + 3)
# str() use to convert string 
# print(full + "3")
# print(full + str(3))
# it is number of term print string using  * 
# print(full * 3)

# string formating ...............

# python 3 
# print("hello {} your last name is {}".format(first,last))
# print("hello {} your last name is {}".format(first,last*3))

# python 3.6
# never forget write "f" 
# print(f"hello {first} your last name is {last} ")
# print(f"hello {first} your last name is {last * 2} ")

# indexing ...............
# Alok
# A = 0 = -4
# l = 1 = -3
# o = 2 = -2
# k = 3 = -1 
# a = "ram"
# print(a[2])
# print(a[-3])



# string slicing.............
# syntax:- [start argument : last argument]
# lang = "python"
# print(lang[0 : 4])
# print(lang[ : ])
# print(lang[-2 : 3])
# print(lang[1:])
# print(lang[: 3])


# step argument slicing.............
# mean it is give gap of character 
# syntax:- [start argument : last argument: step argument]         


print("Ramayan"[0:4:2])
print("Ramayan"[0:6:2])
print("Ramayan"[0:7:3])
print("Ramayan"[3::-1])
print("Ramayan"[-1::-1])
print("Ramayan"[::-1])
