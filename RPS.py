from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
user = False

while user == False:
#set player to True
    user = input("Rock, Paper, Scissors?")
    if user == computer:
        print("Tie!")
    elif user == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", user)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", user)
        else:
            print("You win!", player, "covers", computer)
    elif user == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", user)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    user = False
    computer = t[randint(0,2)]