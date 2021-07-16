# coroutins hum tab use karte hai jab hamara function aisa hai ki use intialise hone time lagata hai 
# to use ek bar intialise karne ke bad any time any place use kar sake

def searcher():
    import time
    # some 4 seconds time consuming task
    book = 'This is a book on harry and code with harry and good'
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print('Your text is in the book')
        else:
            print('Text is not in the book')

search = searcher()
print('search started ')
next(search)
print("next method run")
search.send('harry')

# coroutins close or relese resource
search.close()
## search.send('harry')




# Chalenge,,,........
print()
print()


def finder():
    import time 
    letter = 'How are you alok , i am better , what you do .'
    time.sleep(3)

    while True:
        value = (yield)
        if value in letter:
            print('your text are found')
        else:
            print('your text not found')
        
find = finder()
next(find)
val = input('Enter your text : ')
find.send(val)
