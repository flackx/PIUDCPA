import random

list = ["rock","paper","scissors"]
val1 = input("Choose rock,paper or scissors : ")
computerchoice = random.choice(list)

if computerchoice == val1:
    print("Its a draw. You both picked the same")
elif computerchoice == "rock" and val1 == "paper":
    print("Congratulations, you won!")
elif computerchoice == "rock" and val1 == "scissors":
    print("Oh no, looks like the computer has won")
elif computerchoice == "paper" and val1 == "scissors":
    print("Congratulations, you won!")
elif computerchoice == "paper" and val1 == "rock":    
    print("Oh no, looks like the computer has won")
elif computerchoice == "scissors" and val1 == "rock":    
    print("Congratulations, you won!")
elif computerchoice == "scissors" and val1 == "paper":    
    print("Oh no, looks like the computer has won")