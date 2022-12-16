import app
import os

os.system('cls')
print("********************************************************************\nWelcome to Rock, Paper and scissors Game")

score = 0

pl = input("\nEnter your choice\n1. Press '1' for Rock.\n2. Press '2' for Paper.\n3. Press '3' for Scissors.\nEnter  \"No\" for exiting\n ")

if(pl[0] == 'n' or pl[0] == 'N'):
    app.ext(score)

while pl[0] != 'n' or pl[0] != 'N':
    
    while (ord(pl[0]) > 51) or (ord(pl[0]) < 49):
        os.system('cls')
        print("\nWRONG CHOICE!!!!\n")
        pl = input("\nEnter your choice\n1. Press '1' for Rock.\n2. Press '2' for Paper.\n3. Press '3' for Scissors.\nEnter \"No\" for exiting\n")
        if(pl[0] == 'n' or pl[0] == 'N'):
            app.ext(score)
    os.system('cls')
    score += app.play(int(pl[0]))
    print(f"\nYour current score is {score} ")
    pl = input("\nEnter your choice\n1. Press '1' for Rock.\n2. Press '2' for Paper.\n3. Press '3' for Scissors.\nEnter  \"No\" for exiting\n ")

if(pl[0] == 'n' or pl[0] == 'N'):
    app.ext(score)
