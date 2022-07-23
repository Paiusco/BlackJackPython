from player import Player, hit_me


def _deals_cards(player, number_of_cards=1):
    player.draw_cards(number_of_cards=number_of_cards)


def _player_has_blackjack(player):
    return player.has_blackjack()


def _show_player_card(player, number_of_cards):
    if number_of_cards == 0:
        player.show_all_cards()
    else:
        player.show_one_card()


def _calculate_player_score(player):
    return player.get_current_score()


def _highest_score(pc_score, user_score):
    print(f"Your score:{user_score}, Computer Score: {pc_score}")
    if pc_score == user_score:
        print("Draw!")
    elif pc_score > user_score:
        print("Computer won!")
        return
    else:
        print("You won!")


def _show_player_score(player):
    print(f"Current score: {_calculate_player_score(player)}")


class BlackJack:
    BLACKJACK_VALUE = 21
    COMPUTER_THRESHOLD = 16

    def __init__(self, player_name):
        self._user = Player(player_name)
        self._computer = Player()

    def play(self):
        # First turn
        winner_on_first_turn = self._first_turn()
        if winner_on_first_turn is not None:
            return winner_on_first_turn

        # User turn
        winner_on_round = self._user_turn()
        if winner_on_round is not None:
            return winner_on_round

        # Computer turn
        winner_on_round = self._computer_turn()
        if winner_on_round is not None:
            return winner_on_round

        # Last turn
        return self._find_winner()

    def _find_winner(self):
        computer_score = _calculate_player_score(self._computer)
        user_score = _calculate_player_score(self._user)
        print(f"Your score:{user_score}, Computer Score: {computer_score}")
        if computer_score == user_score:
            return None
        elif computer_score > user_score:
            return self._computer
        else:
            return self._user

    def _computer_turn(self):
        while _calculate_player_score(self._computer) < BlackJack.COMPUTER_THRESHOLD:
            _deals_cards(self._computer)
        score = _calculate_player_score(self._computer)
        if score > BlackJack.BLACKJACK_VALUE:
            print(f"Computer reached more {BlackJack.BLACKJACK_VALUE}")
            return self._user

    def _user_turn(self):
        while hit_me():
            _deals_cards(self._user)
            _show_player_card(self._user, 0)
            _show_player_score(self._user)
        score = _calculate_player_score(self._user)
        if score > BlackJack.BLACKJACK_VALUE:
            print(f"You reached more than {BlackJack.BLACKJACK_VALUE}")
            return self._computer

    def _first_turn(self):
        _deals_cards(self._user, 2)
        _deals_cards(self._computer, 2)
        _show_player_card(self._user, 0)
        _show_player_score(self._user)
        _show_player_card(self._computer, 1)

        if self._computer.has_blackjack():
            print("The computer won with BlackJack!")
            return self._computer
        elif _player_has_blackjack(self._user):
            print(f"The {self._user.name} won with BlackJack!")
            _show_player_card(self._computer, 0)
            return self._user
