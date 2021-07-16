# csv = comma seperated value
# isme data ko table ki form me store karti hai
# example -> 
# name,email,mobile no # first row say 'head' 
# alok,alokjaiswl@gail.com,2445366656
# alok,alokjaiswl@gail.com,2265763545

# jaruri nahi hai ki , hi use kare * | etc use kar sakte hai

# use CSV file import some module
from csv import reader # dicwriter class bhi use kar sakte hai

# with open('file.txt', 'r') as f:
#     csvReader = reader(f)
#     # iterator hai
#     # print(csvReader)
#     for row in csvReader:
#         print(row)


from csv import DictReader
# ordered dict
with open('file.txt', 'r') as f:
    csvReader = DictReader(f) # when you want not use comma DictReader(f,delimiter='|') and in file use '|' 
    for row in csvReader:
        #print(row[])
        print(row['email'])


