import random
#from xml.etree.ElementTree import QName

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]

options[0]

while True:
    user_input=input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        
        break
    if user_input  not in options:
        print('invalid choice!Try again.')
        continue
        
    random_number= random.randint(0,2)
      #0=Rock,1=Paper,2=scissors
    computer_pick=options[random_number]
    print("computer picked",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
       print("You won!")
       user_wins += 1
       continue

    elif user_input == "scissors" and computer_pick == "paper":
       print("You won!")
       user_wins += 1
       continue

    elif user_input == "paper" and computer_pick == "rock":
       print("You won!")
       user_wins += 1
       continue
    else:
        print("You lost!")
        computer_wins += 1
print("You won", user_wins , "times.")
print("The computer won", computer_wins , "times.")
print("Goodbye")
