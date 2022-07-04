import random

from deck import DECK


def hit_me():
    answer = input('Do you want to draw more cards?(yes/no)\n').casefold()
    if answer != 'yes':
        return False
    return True


class Player:

    def __init__(self, name=None):
        self.name = name
        self._cards = []

    def show_all_cards(self):
        self._show_cards(0)

    def show_one_card(self):
        self._show_cards(1)

    def draw_cards(self, number_of_cards):
        self._cards.extend(random.sample(DECK, number_of_cards))

    def has_blackjack(self):
        if len(self._cards) != 2:
            return False
        if 10 in self._cards and 1 in self._cards:
            return True
        return False

    def get_current_score(self):
        current_score = 0
        for card in self._cards:
            if card == 1:
                current_score += 11
            else:
                current_score += card
        if current_score > 21 and 1 in self._cards:
            current_score -= 10
        return current_score

    def _show_cards(self, number_of_cards=1):
        print(f"Card(s) of {self.name}:")
        if number_of_cards == 0:
            print(self._cards)
        else:
            print(self._cards[0:number_of_cards])
        print()
