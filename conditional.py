age = int(input("enter your age "))
#if age >= 14:
#   print("you are able to play")

# pass statement: when we want if block empty, simply write pass
if age >= 14:
    pass
  
if age >= 14:
   print("you are able to play")
else:
       print("you are not able to play")

# and, or operator
name = "abc"
age1 = 15
if name == "abc" and age1 == 13 :
    print("condition true")
else:
      print("condition false")   

if name == "abc" or age1 == 13 :
    print("condition true")
else:
    print("condition false")       

# if elif else staement ... . ........ .  .
# show ticketing price 
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above  60 (200)

if 0<age<=3:
    print("ticket free")
elif 3<age<=10:
     print("ticket rs. 150")
elif 11<age<=60:
    print("ticket rs. 250")
else:
    print("ticket rs. 200")       


# in keyword 
# to check character are find in string or not
if 'a' in "slok":
    print("a is preset in sttring")
else:
    print("not present")    


# check empty or not
# important
name = input("enter your name ")
if name :
  print(f"your name {name}")
else:
    print("you did not enter name ")  