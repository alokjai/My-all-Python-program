name = "AloK jAiSwaL"

# length method
print(len(name))

# lower method
print(name.lower())

# uppper method
print(name.upper())

# title method
print(name.title())

# count method (term of character count this method)
print(name.count("A"))

# remove space using strip() as like trim()................................

name1 = "     Alok jaiswal         "

print(name1)
print(name1.strip())
# left side remove space
print(name1.lstrip())
# right side remove space
print(name1.rstrip())


# remove space inside string ......use replace()
print(name1.replace(" ", ""))


# Replace() method ..................
sentence = "she is good dancer.she is good manners."
print(sentence)
print(sentence.replace(" ", "_"))
print(sentence.replace("is", "was"))
# when we want only one or two or more  word replace. given below
print(sentence.replace("is", "was",1))

# find() method.................................
# it return position(index no.) of character in string, where (parameter)string's character start
print(sentence.find("is", 15))

# center() Method ....................................
# this method fill string in ceenter 
name2 = "slok"
print(name2.center(10,"#"))
print(name2.center(len(name2) + 8,"#"))

# type method
s = "alok"
print(type(s))