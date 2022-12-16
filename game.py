import app

print("********************************************************************\nWelcome to Rock, Paper and scissors Game")

score = app.play()
print(f"\nCurrent score is {score}\n ")
gh = 0
c = input("\nwanna play again ?\n [Y/N]:-\n")

while c == 'y' or c == 'Y':
    score += app.play()
    print(f"\nCurrent score is {score}\n ")
    c = input("\nwanna play again ?\n [Y/N]:-\n")
    
if c!= 'y':
    print(f"\nThanks for playing and your score is {score} \n")
    gh = input("pressing any key and enter will end the game")
