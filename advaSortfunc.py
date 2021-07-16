# advance sort function
# sort() tuple ko sort nahi karta,kyunki tuple are immutable
# but sorted() tuple ko sort me print karta hai lekin usme change nahi karta 

fruits = ['grapes','mango','lichy'] 
# fruits.sort()
# print(fruits)

sorted(fruits)
print(fruits)


# advance ..................................

guiter = [
    {'model': 'yamaha f310','price':8400},
    {'model': 'faith naptune','price':50000},
    {'model': 'faith apollo venus ','price':35000},
    {'model': 'taylor 814','price':450000}
]

print(sorted(guiter, key= lambda di: di['price'],reverse= True))

asd = sorted(guiter, key= lambda di: di['price'],reverse= True)
print(asd)





