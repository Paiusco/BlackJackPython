from Menu import print_initial_menu
from Player import Player, hit_me


def _deals_cards(player, number_of_cards=1):
    player.draw_cards(number_of_cards=number_of_cards)


def _player_has_blackjack(player):
    if player.has_blackjack():
        return True
    return False


def _show_player_card(player, number_of_cards):
    player.show_cards(number_of_cards)


def _calculate_player_score(player):
    return player.get_current_score()


def _find_winner(pc_score, user_score):
    print(f"Your score:{user_score}, Computer Score: {pc_score}")
    if pc_score == user_score:
        print("Draw!")
    elif pc_score > user_score:
        print("Computer won!")
    else:
        print("You won!")


class BlackJack:

    def __init__(self, player_name):
        self._user = Player(player_name)
        self._computer = Player("Computer")
        print_initial_menu()

    def play(self):
        _deals_cards(self._user, 2)
        _deals_cards(self._computer, 2)

        _show_player_card(self._user, 0)

        if _player_has_blackjack(self._computer):
            print("The computer won with BlackJack!")
            return
        if _player_has_blackjack(self._user):
            print(f"The {self._user.name} won with BlackJack!")
            return

        _show_player_card(self._computer, 1)

        while hit_me():
            _deals_cards(self._user)
            _show_player_card(self._user, 0)
            score = _calculate_player_score(self._user)
            if score > 21:
                print("You lost!")
                return

        while _calculate_player_score(self._computer) < 16:
            _deals_cards(self._computer)
            score = _calculate_player_score(self._computer)
            if score > 21:
                print("You won!")
                return

        pc_score, user_score = self._calculate_players_scores()
        _find_winner(pc_score, user_score)

    def _calculate_players_scores(self):
        pc_score = self._computer.get_current_score()
        user_score = self._user.get_current_score()
        return pc_score, user_score
