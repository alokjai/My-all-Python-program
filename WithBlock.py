# with block
# context manager

# with open('helloworld.txt') as f:
#     data = f.read()
#     print(data)
# print(f.closed)



# write to file
# mode - w(write) ,r+(read & write) ,a(append) , r(read)
with open('helloworld2.txt', 'r+') as f:
   f.seek(len(f.read()))
   f.write('please call\n')



# read one file & write another file 
with open('helloworld.txt','r') as rf:
    with open('file.txt', 'w') as wf:
        wf.write(rf.read())





