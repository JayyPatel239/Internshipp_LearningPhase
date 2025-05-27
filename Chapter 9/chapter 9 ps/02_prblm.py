'''
The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi
score whenever the game() function breaks the Hi-score. 
'''

def game():
    import random
    print("Playing the game...")
    print("Game in progress...")
    with open("Chapter 9/chapter 9 ps/hiscore.txt", "r") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    score =random.randint(0, 100)  # Simulating a game score between 0 and 100
    print(f"Your score is: {score}")
    if (score>hiscore):
        print("Congratulations! You have broken the Hi-score.")
        with open("Chapter 9/chapter 9 ps/hiscore.txt", "w") as f:
            f.write(str(score))
        
# when you do in write mode it will accept string only
game()