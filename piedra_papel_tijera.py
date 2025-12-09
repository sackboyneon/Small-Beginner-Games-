import random
print("Welcome to Rock, Paper, Scissors Game!")

player = input("Do you want to play?: ")

if player == "no":
    print("Thanks for playing! Goodbye.")


while player == "yes":
    player= (input("Pick rock, paper or scissors: "))
    decisions = ["rock", "paper", "scissors"]
    decisions_computer = random.choice(decisions)
    print(decisions_computer)

    if decisions_computer == "paper" and player == "paper":
        print("Its a tie")
    elif decisions_computer == "rock" and player == "rock":
        print("Its a tie")
    elif decisions_computer == "scissors" and player == "scissors":
        print("Its a tie")

    elif decisions_computer == "paper" and player == "scissors":
        print("You win!")
    elif decisions_computer == "rock" and player == "paper":
        print("You win!")
    elif decisions_computer == "scissors" and player == "rock":
        print("You win!")

    elif decisions_computer == "scissors" and player == "paper":
        print("You lose!")
    elif decisions_computer == "paper" and player == "rock":
        print("You lose!")
    elif decisions_computer == "rock" and player == "scissors":
        print("You lose!")

    player = input("Do you want to play again? ")
    if player == "no":
        print("Thanks for playing! Goodbye.")



