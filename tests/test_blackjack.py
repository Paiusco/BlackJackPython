import unittest
import unittest.mock
from unittest import mock

import blackjack


class BlackJackTest(unittest.TestCase):

    def setUp(self) -> None:
        self._blackjack = blackjack.BlackJack("TestPlayer")

    def test_winner_computer_blackjack(self):
        with mock.patch.object(self._blackjack._computer, 'has_blackjack', return_value=True):
            self.assertEqual(self._blackjack.play(), self._blackjack._computer)

    def test_winner_user_blackjack(self):
        with mock.patch.object(self._blackjack._computer, 'has_blackjack', return_value=False):
            with mock.patch.object(self._blackjack._user, 'has_blackjack', return_value=True):
                self.assertEqual(self._blackjack.play(), self._blackjack._user)
    #
    # def test_winner_computer_score(self):
    #     self.assertEqual(self._blackjack.play(), self._blackjack._computer)
    #
    # def test_winner_user_score(self):
    #     # Mock player return
    #     self.assertEqual(self._blackjack.play(), self._blackjack._computer)
    #
    # def test_winner_draw(self):
    #     # Mock player return
    #     self.assertEqual(self._blackjack.play(), 0)


if __name__ == '__main__':
    unittest.main()
