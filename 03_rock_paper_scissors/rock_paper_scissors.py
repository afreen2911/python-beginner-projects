import random
choices=["rock", "paper",  "scissors"]
computer_choice=random.choice(choices)
user_choice=input("choose rock,paper, or scissors:").lower()

if user_choice==computer_choice:
    print("Draw")
elif (user_choice=="rock" and computer_choice=="scissors") or (user_choice=="scissors" and computer_choice=="paper") or (user_choice=="paper" and computer_choice=="rock"):
    print("You Won")
else:
    print("Computer Won")