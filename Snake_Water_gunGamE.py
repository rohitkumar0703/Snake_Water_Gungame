'''We all have played snake, water gun game in our childhood. If you haven’t,
 google the rules of this game and write a Python program capable of playing 
 this game with the user.'''

import random

def play_game():
    choice = ['snake', 'water', 'gun']

    print("Welcome to snake water gun Game!")
    print("Choose one of the following: snake, water, or gun.")
    print("You will play against the computer. ")

    while True:
        # player's Choice
        players_choice = input("Your turn: ").lower()
        if players_choice not in choice:
            print("Invalid Input! Please choose again,")
            continue

        # Computer's choice
        computer_choice = random.choice(choice)

        print("Computer's turn: ", computer_choice)

        #Determine the winner
        if players_choice == computer_choice:
            print("It's a tie!")
        elif players_choice == "snake":
            if computer_choice == "water":
                print("You win! Snake drinks water.")
            else:
                print("You lose! Gun kills snake.")
        elif players_choice == "water":
            if computer_choice == "gun":
                print("You win! Water douses the gun. ")
            else:
                print("You lose! Snake drinks water.")
        elif players_choice == "gun":
            if computer_choice == "snake":
                print("You win! Gun kills snake.")
            else:
                print("You lose! Water douses the gun.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

play_game()  