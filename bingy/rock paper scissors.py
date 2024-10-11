import random

def print_rules():
    print("The computer will think of either rock paper or scissors.")
    print("You will enter the r for rock, p for paper or s for scissors.")
    print("The computer will reveal it's choise and the winner.")

def play_game():
    player_letter = input("enter r for rock, p for paper or s for scissors: ").lower()
    computer_choice = random.randint(0,2) # 0=rock 1=paper 2=scissors
    
    if computer_choice == 0:
        print("The computer chose: Rock")
    elif computer_choice == 1:
        print("The computer chose: Paper")
    else:
        print("The computer chose: Scissors")

    if player_letter == "r":
        player_choice = 0
    elif player_letter == "p":
        player_choice = 1
    elif player_letter == "s":
        player_choice = 2

    if computer_choice == player_choice:
        print("It's a draw!")
    elif computer_choice == 0 and player_choice == 1:
        print("Player Wins!")
    elif computer_choice == 0 and player_choice == 2:
        print("Computer Wins!")
    elif computer_choice == 1 and player_choice == 2:
        print("Player Wins!")
    elif computer_choice == 1 and player_choice == 0:
        print("Computer Wins!")
    elif computer_choice == 2 and player_choice == 0:
        print("Player Wins!")
    elif computer_choice == 2 and player_choice == 1:
        print("Computer Wins!")

game_active = True

print("Welcome to the Rock, Paper, Scissors Game")
print("-----------------------------------------")
print_rules()

while game_active == True:
    play_game()
    if game_active == False:
        break

input("Press enter to exit.")