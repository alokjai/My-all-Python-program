# Exception handling
# try except else finally

# while True:
#     try:
#        age = int(input('enter your age: '))
#        break
#     except ValueError:
#        print("invalid input")

#     except NameError:
#        print("invalid input") 

#     except:
#        print("invalid input")      


# if age < 18:
#     print('you can\'t play this game.')
# else:
#     print('you can play this game')    

# else and finally clause,,,,,,,,,,,,,,,,,,,,,

while True:
    try:
       num = int(input('enter number: '))

    except ValueError:
        print('you did\'t entered integer')
    except:
        print('unexpected error...')    

    else:
        print(f'user input = {num}')
        break    
    
    finally:
        print('this is finally block....')





