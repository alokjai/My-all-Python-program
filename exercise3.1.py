# number guessing game
import random
winnum = random.randint(0,50)
guess = int(input("guess number between 1 to 50 "))
if winnum == guess:
    print("you are win")
else:
    if guess > winnum:
        print("too high")
    else:
         print("too low")
            