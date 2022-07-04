import unittest

from player import Player


class PlayerTest(unittest.TestCase):

    def setUp(self) -> None:
        self._player = Player(name="Test")

    def _force_draw_card(self, card_to_draw):
        self._player._cards.append(card_to_draw)

    def test_draw_cards(self):
        self.assertEqual(len(self._player._cards), 0)
        self._player.draw_cards(1)
        self.assertEqual(len(self._player._cards), 1)
        self._player.draw_cards(1)
        self.assertEqual(len(self._player._cards), 2)

    def test_score_without_special_cases(self):
        self._force_draw_card(2)
        self._force_draw_card(2)
        self.assertEqual(self._player.get_current_score(), 4)

    def test_score_with_ten(self):
        self._force_draw_card(10)
        self._force_draw_card(2)
        self.assertEqual(self._player.get_current_score(), 12)

    def test_score_with_ace_equal_21(self):
        self._force_draw_card(10)
        self._force_draw_card(1)
        self.assertEqual(self._player.get_current_score(), 21)

    def test_score_with_ace_bigger_than_21(self):
        self._force_draw_card(10)
        self._force_draw_card(5)
        self._force_draw_card(1)
        self.assertEqual(self._player.get_current_score(), 16)

    def test_score_with_ace_less_than_21(self):
        self._force_draw_card(4)
        self._force_draw_card(5)
        self._force_draw_card(1)
        self.assertEqual(self._player.get_current_score(), 20)

    def test_score_with_ace_changing_value(self):
        self._force_draw_card(1)
        self._force_draw_card(3)
        self.assertEqual(self._player.get_current_score(), 14)
        self._force_draw_card(8)
        self.assertEqual(self._player.get_current_score(), 12)

    def test_has_blackjack(self):
        self._force_draw_card(10)
        self._force_draw_card(1)
        self.assertTrue(self._player.has_blackjack())

    def test_has_blackjack(self):
        self._force_draw_card(5)
        self._force_draw_card(2)
        self.assertFalse(self._player.has_blackjack())

    def test_jackeline2(self):
        self._force_draw_card(1)
        self._force_draw_card(1)
        self.assertEqual(self._player.get_current_score(), 12)
        self._force_draw_card(1)
        self.assertEqual(self._player.get_current_score(), 23) #?


if __name__ == '__main__':
    unittest.main()
