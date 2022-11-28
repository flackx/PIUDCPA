import random
#Massive problem fixed for code so we do hotfix


while True:
    user_action = input("Choose rock,paper or scissors : ")
    list1 = ["rock", "paper", "scissors"]
    val1 = random.choice(list1)
    print(f"\nYou chose {user_action}, computer chose {val1}.\n")

    if user_action == val1:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if val1 == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if val1 == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if val1 == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break