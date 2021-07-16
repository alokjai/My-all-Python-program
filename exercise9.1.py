# exercise decorator

# @calculatetime
# def func():
#    print('this is function')

# func()
# this function took 3 sec to run

import time
from functools import wraps
def calculatetime(function):
    @wraps(function)
    def wraper(*args,**kwargs):
        print(f"function name is {function.__name__}")
        print()
        t1 = time.time()
        function(*args,**kwargs)
        print()
        t2 = time.time()
        
        print(f"this function took {t2-t1} sec to run")
        return function
    return wraper    

@calculatetime
def func(a):
    for l in range(1,6):
       print(f"this is a function {l}")
 

func('alok')









