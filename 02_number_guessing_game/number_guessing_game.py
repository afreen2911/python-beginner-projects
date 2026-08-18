import random
while True:
    number=random.randint(1,100)
    attempts=0
    max_attempts=7

    print("======== NEW GAME ==========")
    print("You have", max_attempts, "attempts.")
    while True:
        
        guess=int(input("Guess a number between 1 and 100:"))
        attempts +=1
        
        if guess==number:
            print("correct!")
            print("you guessed the number in", attempts, "attempts")
            break
            
        elif guess>number:
            print("Too High! Try Again.")
        else:
            print("Too Low! Try Again.")

        if attempts==max_attempts:
            print("Game Over!")
            print("The number was", number)
            break
        
    choice=input("DO YOU WANT TO PLAY AGAIN Y/N:")
    if choice.upper()=="N":
        break

    