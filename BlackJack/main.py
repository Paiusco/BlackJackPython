from blackjack import BlackJack
from menu import ask_player_name_input, ask_player_play_again, print_ending_menu, print_initial_menu, show_winner

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_initial_menu()
    _running = True
    while _running:
        player_name = ask_player_name_input()
        bj = BlackJack(player_name=player_name)
        winner = bj.play()
        show_winner(winner)
        _running = ask_player_play_again()

    print_ending_menu()
