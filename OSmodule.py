import os
# os.getcwd()   #....cwd == current working directory
print(os.getcwd())

# change current working directory
# os.chdir(r'E:\mechanical je')
# print(os.getcwd())


# make folder 
#os.mkdir('javaFadu')

# check exist file
print(os.path.exists('javaFadu'))

# file create

#open('alok.txt','a').close()

# return all file & folder list
# print(os.listdir())
# print(os.listdir(r'E:\mechanical je'))


# check file in depth.......
# fileiter = os.walk(r'D:\MOVIE')
# for current_path, folder_name, file_name in fileiter:
#     print(f'current path : {current_path}')
#     print(f'folder name : {folder_name}')
#     print(f'file name : {file_name}')


# delete empty folder........
#os.rmdir('new')


# make folder under folder
#os.makedirs('new/movies')

# shutil module hai jiska function rmtree() folder / file ko parmanently delete karta hai
import shutil
#shutil.rmtree('new/movies')

# copy folder to another folder
shutil.copytree('new','javaFadu') # new == 'copy folder' javaFADU == 'target folder'


# kisi file ko copy karna 

shutil.copy('new/file.txt','javaFadu/Document/copyfile.txt')


#  kisi file ko move  karna 
# shutil.move('file.txt','new/file2.txt')

# move folder
#shutil.move('new', 'new2')
