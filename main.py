from BlackJack import BlackJack
from Menu import ask_player_name_input, ask_player_play_again, print_ending_menu

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    _running = True
    while _running:
        player_name = ask_player_name_input()
        bj = BlackJack(player_name=player_name)
        bj.play()
        _running = ask_player_play_again()

    print_ending_menu()
