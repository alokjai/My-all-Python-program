# writer , Dictwriter

# from csv import writer
# with open('csvfile.csv','w',newline='') as f: # use newline to remove blank line
#     csvWriter = writer(f)
#     # method = writerow, writerows
#     csvWriter.writerow(['name','country'])
#     csvWriter.writerow(['Ram','India'])
#     csvWriter.writerow(['scott','england'])
#     csvWriter.writerow(['jack','french'])

#     csvWriter.writerows([['name','country'],['Ram','India'],['scott','england'],['jack','french']])




from csv import DictWriter # isme pahle hi header insert karaya jata hai 
with open('csvfile2.csv','w',newline='') as f: # use newline to remove blank line
    csvWriter = DictWriter(f,fieldnames=['firstname','lastname','age'])
    csvWriter.writeheader()

    # csvWriter.writerow({
    #     'firstname':'alok',
    #     'lastname':'jaiswal',
    #     'age' : 23
    # })
    # csvWriter.writerow({
    #     'firstname':'amit',
    #     'lastname':'gupta',
    #     'age' : 21
    # })
    # csvWriter.writerow({
    #     'firstname':'amar',
    #     'lastname':'yadav',
    #     'age' : 23
    # })

# writerows ----> [{},{},{}]

csvWriter.writerows([
    {'firstname':'alok','lastname':'jaiswal','age':21},
    {'firstname':'amit','lastname':'jaiswal','age':24},
    {'firstname':'amar','lastname':'jaiswal','age':23}
])





