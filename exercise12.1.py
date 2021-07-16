

def divide(a,b):
    try:
        return a/b
    except ValueError:
        print('please input number only')
    except ZeroDivisionError:
        print('please don\'t divide by zero')



print(divide(12,4))                