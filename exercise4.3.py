# fibonacci series

def fibo():
    i=0
    a=0
    b=1
    while i < 10:   
        c = a+b
        a = b
        b = c  
        print(b)
        
        i +=1


fibo()        