# problem
# ask user for name
# example : "alok"
# print count of  each words

name = input("enter your name ")
i=0
temp = ""
while i<len(name):
    if name[i] not in temp:
      temp = temp + name[i]
      n = name.count(name[i])
      print(f"In {name} {name[i]} are {n} time") 
    i = i+1
  