# dictionary comprehension
# square = {1:1, 2:4, 3:9}

square = {num:num**2 for num in range(1,11)}
print(square)

square = {f"square of {num} is":num**2 for num in range(1,11)}
for k,v in square.items():
    print(f"{k}:{v}")


# character count
string = "amar"
wordCount = {char:string.count(char) for char in string}
print(wordCount)



# dic. comprehension with if-else
# d = {1:'odd, 2:'even'}

oddEven = {i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(oddEven)

