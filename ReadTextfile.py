# readfile
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method

# f = open('helloworld.txt') # f yahan ek itrator hai (loop chal sakta hai ispar)
# print(f.read())
# f.close()

# tell function(),,,,,,,,,,,,,,,,,,,,


# f = open('helloworld.txt')
# print(f'cursor position . {f.tell()}')
# print(f.read())
# print(f'cursor position . {f.tell()}')
# f.close()

# seek() function

# f = open('helloworld.txt')
# print(f'cursor position . {f.tell()}')

# print(f.read())
# print(f'cursor position . {f.tell()}')
# print('before seeek method ')
# f.seek(0)
# print('after seeek method ')
# print(f'cursor position . {f.tell()}')
# print(f.read())
# f.close()

# readline() function

# print(f.readline(), end='')
# print(f.readline())
# print(f.readline())

# readlines() function
# lines = f.readlines()
# print(lines)
# print(len(lines))

# for line in lines:
#     print(line, end='')



# f = open('helloworld.txt')
# # data descripter - name , closed 
# print(f.name) # show file name
# print(f.closed) # kyunki abhi file close nahi ki isliye false aayega 
# f.close()

# jab file kisi aur place par ho tab
# file = open("D:\dataase url.txt") # yahan par error ayega kyunki window path ke liye 
# '\' ka use karta hai aur python ise esc sequence ke taur par lega jisase error aayegi

file = open(r"D:\dataase url.txt")
print(file.read())
file.close()
