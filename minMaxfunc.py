# Advanced min() and max()


name = ['alok','mohit','suraja']

def func(item):
    return len(item)

print(min(name))
print(min(name, key = func)) # yahan function ke aadhar par max nikala gaya hai

print(max(name,key=lambda item : len(item)))

# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


std1 = {
    'harshit' : {'score' : 90,'age' : 24},
    'alok' : {'score' : 60,'age' : 25},
    'amar' : {'score' : 75,'age' : 21}
}

print(max(std1,key=lambda item:std1[item]['age']))

std2 = [
    {'name':'harshit','score':90,'age':24},
    {'name':'alok','score':60,'age':20},
    {'name':'amar','score':75,'age':26}
]

print(max(std2,key=lambda item: item.get('age'))['name'])

