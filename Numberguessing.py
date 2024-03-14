import math
import random
#Range for Values
lower=int(input("Enter lower bound:-"))
upper=int(input("Enter Upper Bound:-"))
#Generating a Random number in the given range using Random Module 
num=random.randint(lower,upper)
k=round(math.log(upper - lower + 1, 2))
print("User has got only",k,"Chances to guess")
#Initialising Chances 
chances=0
while chances < k:
    chances+=1
    #Inputting Number from Player
    guess=int(input("Enter your'e guess"))
    
    if num==guess:
        print("you Guessed correctly in ",chances,"Chances")
        break
    elif num<guess:
        print("Guess is higher")
    else:
        print("Guess is Lower")
    
    #Condition for chances Excedded
    if chances>=k:
        print(k,"Chances Excedded")
        print("Better Luck Next time")
    
    
    


