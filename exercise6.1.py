
# define a function that  takes a number(num)
# return a dictionary containing cube of numbers from 1 to num

def cubeFinder(num):
    
    cube = {}
    for i in range(1,num+1):
      cube[i] = i**3
    return cube

print(cubeFinder(4))



# character counter

def counter(c):   
    counts = {}
    for char in c:
      counts[char] = c.count(char)
    return counts

print(counter('alka'))