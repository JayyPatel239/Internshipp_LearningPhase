'''
We all have played snake, water gun game in our childhood. If you haven’t, google the 
rules of this game and write a python program capable of playing this game with the 
user. 

1 for snake, -1 for water, 0 for gun
'''

import random

youdict = {
    "snake": 1,
    "water": -1,
    "gun": 0
}

# Random choice for computer
computer = random.choice([1, -1, 0])


youstr = input("Enter your choice (snake, water, gun): ").strip().lower()

if youstr not in youdict:
    print("Invalid input. Please enter 'snake', 'water', or 'gun'.")
else:
    you = youdict[youstr]
    comp_str = [k for k, v in youdict.items() if v == computer][0]

    print(f"You chose: {youstr}")
    print(f"Computer chose: {comp_str}")

    if you == computer:
        print("It's a tie!")
    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        print("You win!")
    else:
        print("You lose!")
