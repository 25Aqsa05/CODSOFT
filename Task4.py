# game for rock pper scissor

import random
user_score=0
computer_score=0
choice=['rock','paper','scissor']
while True:
    print("Choose any one :rock,paper,scissor ")
    user_choice=input("your choice :").lower()

    computer_choice=random.choice(choice)
    print(f"Computer choice is : {computer_choice}")
    if user_choice not in choice:
        print("invalid choice.TRY AGAIN!")
        continue
    if user_choice==computer_choice:
        print("It is a tie")
    elif (user_choice == 'rock' and computer_choice == 'scissor') or (user_choice == 'scissor' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        print("user wins")
        user_score+=1
    else:
        print("Computer wins")
        computer_score+=1
    print(f"Your score - {user_score},Computer Score - {computer_score}")
    again_play=input("Enter yes if you want to play again").lower()
    if(again_play!= 'yes'):
        print("Thanks for playing.")
        break 