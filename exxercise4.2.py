# check palindrom word

# def palindrom(name):
#     i = 1
#     dup = ""
#     while i <= len(name):
#        dup += name[-i]
#        i = i+1
#     if name == dup:
#         return f"{name} is palindrome" 
#     else:  
#         return f"{name} is not palindrom"    

# def palindrom(word):
#     reve = word[ : :-1]
#     if word == reve:
#         return True
#     else:
#         return False  
def palindrom(word):
    return word == word[::-1] 

name = input("enter word to check palindrom ")
print(palindrom(name))


   