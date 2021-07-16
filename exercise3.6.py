# modify number guessing game
import random
winnum = random.randint(0,50)
gameOver = False
guessnum = 1
guess = int(input("guess number between 1 to 50 "))
while not gameOver:
 if winnum == guess:
    print(f"you are win, you guess in {guessnum} time ")
    gameOver = True
 else:
    if guess > winnum:
        print("too high")
       
    else:
         print("too low")
    guessnum +=1
    guess = int(input("guess  again : "))