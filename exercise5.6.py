

num = [12,3,54,[1,2,3,43]]

def checklist(lst):
    n = 0
    for l in lst:
        if type(l) == list:
            n += 1
    return n

print(checklist(num))