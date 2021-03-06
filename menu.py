import os


def print_initial_menu():
    print("Let's play BlackJack")


def print_ending_menu():
    print("Thank you for playing! See ya!")


def ask_player_name_input():
    return input("What's your name?\n")


def ask_player_play_again():
    result = input("Do you want to play again?").lower()
    if result != "yes":
        return False
    os.system("clear")
    return True


def show_winner(winner):
    if winner is None:
        print("There was a Draw!")
    elif winner.name is None:
        print("You lost :(")
    else:
        print("You won! Congrats")
    print()


#
# class Menu:
#
#     def __init__(self):
#         print_initial_menu()
