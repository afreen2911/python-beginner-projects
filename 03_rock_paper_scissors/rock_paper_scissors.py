import random
choices=["rock", "paper",  "scissors"]
computer_score=0
user_score=0
rounds=0
print("========= ROCK PAPER AND SCISSORS GAME =========")
while rounds<3:
    rounds+=1
    print("================ ROUND", rounds, " ================")
    computer_choice=random.choice(choices)
    user_choice=input("choose rock,paper, or scissors:").lower()
    if user_choice==computer_choice:
        print("Draw")
    elif (user_choice=="rock" and computer_choice=="scissors") or (user_choice=="scissors" and computer_choice=="paper") or (user_choice=="paper" and computer_choice=="rock"):
        user_score+=1
        print("You Won")
    else:
        computer_score+=1
        print("Computer Won")
    print("Score")
    print("Your Score:", user_score)
    print("computer score:", computer_score)
print(" <<<<<<<< Results >>>>>>>>")
print("Your Total Score:", user_score)
print("Computer Total Score:", computer_score)

if user_score==computer_score:
    print("IT'S A DRAW")
elif user_score>computer_score:
    print("THAT'S A GREAT BATTLE, YOU WON")
else:
    print("COMPUTER WINS THE GAME!")