import random

from Deck import deck


def hit_me():
    answer = input("Do you want to draw more cards?(yes/no)\n").lower()
    if answer != "yes":
        return False
    return True


class Player:

    def __init__(self, name="Unknown"):
        self.name = name
        self._cards = []

    def show_cards(self, number_of_cards=1):
        print(f"Card(s) of {self.name}:\n")
        if number_of_cards == 0:
            print(self._cards)
        else:
            print(self._cards[0:number_of_cards])

    def draw_cards(self, number_of_cards):
        self._cards.extend(random.sample(deck, number_of_cards))

    def has_blackjack(self):
        if len(self._cards) != 2:
            return False
        if 0 in self._cards and 1 in self._cards:
            return True
        return False

    def get_current_score(self):
        current_score = 0
        for card in self._cards:
            if card == 0:
                current_score += 10
                continue
            if card == 1 and current_score + 11 < 21:
                current_score += 11
                continue
            current_score += card
        return current_score

