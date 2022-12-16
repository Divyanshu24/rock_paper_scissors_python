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

def choose():
    pl = input("\nEnter your choice\n1. Press '1' for Rock.\n2. Press '2' for Paper.\n3. Press '3' for Scissors.\n")
    
    while (ord(pl) > 51) or (ord(pl) < 49):
        print("\nWRONG CHOICE!!!!\n")
        pl = input("\nEnter your choice\n1. Press '1' for Rock.\n2. Press '2' for Paper.\n3. Press '3' for Scissors.\n")
        
    return int(pl)


# pl = int(input("Enter your choice\n1. Press '1' for Rock.\n2. Press '2' for Paper.\n3. Press '3' for Scissors."))

def play():

    player = choose()

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
