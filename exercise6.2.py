# take user input in dictionry and print using for loop

name = input("what is your name ")
age  = input("what is your age ")
favMovie = input("what is your favourite movie ").split(',')
favsong = input("what is your favourite song ").split(',')

info = {}
info['name'] = name
info['age']  = age
info['favMovie'] = favMovie
info['favsong'] = favsong

for key, value in info.items():
    print(f"{key} : {value}")