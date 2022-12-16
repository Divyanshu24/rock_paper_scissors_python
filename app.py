import random

sc = 0

def win():
    print("\nYou win 🎉😎\n")
    return 1


def loose():
    print("\nYou loose 🤦‍♂️😜😂😂😂\n")
    return -1


r ='''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

p = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

s = '''
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  

choice = {1:r, 2:p, 3:s}

def play(j):

    player = j

    print(choice[player])
    
    com = random.randint(1,3)

    print(choice[com])

    if player == com:
        print("It's a draw")
        sc = 0
    elif player == 1 and com == 3:
        sc = win()
    elif player == 2 and com == 1:
        sc = win()
    elif player == 3 and com == 2:
        sc = win()
    else :
        sc = loose()
    
    return sc

def ext(sc):
    print(f"\nThanks for playing with us and your score is {sc}.")
    input(("press enter"))
    exit()