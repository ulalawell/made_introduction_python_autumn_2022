"""
Tests for implementation of tic tac game
"""


import unittest
from unittest import mock
from io import StringIO
import sys

from tic_tac_game import TicTacGame


@mock.patch("sys.stdout", new=StringIO())
class TestString(unittest.TestCase):
    """
    Implementation of class with tests for tic tac game
    """

    def test_01_show_board(self):
        """
        Tests for showing board
        """
        game = TicTacGame()

        game.show_board()
        output = sys.stdout.getvalue().strip().splitlines()

        self.assertEqual(output[0], "-" * 13)
        self.assertEqual(output[1], "| 1 | 2 | 3 |")
        self.assertEqual(output[2], "-" * 13)
        self.assertEqual(output[3], "| 4 | 5 | 6 |")
        self.assertEqual(output[4], "-" * 13)
        self.assertEqual(output[5], "| 7 | 8 | 9 |")
        self.assertEqual(output[6], "-" * 13)

    def test_02_validate_input(self):
        """
        Tests for validation input
        """
        game = TicTacGame()
        with mock.patch("builtins.input", side_effect=["1", "str", "11", "1", "3"]):

            # put X on 1 position
            game.validate_input("X")
            game.show_board()
            output = sys.stdout.getvalue().strip().splitlines()

            self.assertEqual(output[7], "-" * 13)
            self.assertEqual(output[8], "| X | 2 | 3 |")
            self.assertEqual(output[9], "-" * 13)
            self.assertEqual(output[10], "| 4 | 5 | 6 |")
            self.assertEqual(output[11], "-" * 13)
            self.assertEqual(output[12], "| 7 | 8 | 9 |")
            self.assertEqual(output[13], "-" * 13)

            # put O on str position
            game.validate_input("O")
            output = sys.stdout.getvalue().strip().splitlines()
            self.assertEqual(
                output[14],
                "Incorrect input. Enter a number between 1 and 9 to make a move?",
            )

            # put O on 11 position
            output = sys.stdout.getvalue().strip().splitlines()
            self.assertEqual(
                output[15],
                "Incorrect input. Enter a number between 1 and 9 to make a move?",
            )

            # put O on 1 position
            output = sys.stdout.getvalue().strip().splitlines()
            self.assertEqual(
                output[16],
                "This cell is already taken",
            )

            # put O on 3 position
            game.show_board()
            output = sys.stdout.getvalue().strip().splitlines()

            self.assertEqual(output[17], "-" * 13)
            self.assertEqual(output[18], "| X | 2 | O |")
            self.assertEqual(output[19], "-" * 13)
            self.assertEqual(output[20], "| 4 | 5 | 6 |")
            self.assertEqual(output[21], "-" * 13)
            self.assertEqual(output[22], "| 7 | 8 | 9 |")
            self.assertEqual(output[23], "-" * 13)

    def test_03_check_winner(self):
        """
        Tests for checking winner
        """

        # movements for victory X player by rows
        win_rows_movements = (
            ("1", "4", "2", "6", "3", "9"),
            ("4", "1", "5", "2", "6", "8"),
            ("7", "1", "8", "2", "9", "6"),
        )

        for i in range(3):
            with mock.patch("builtins.input", side_effect=win_rows_movements[i]):
                game = TicTacGame()
                game.start_game()
                output = sys.stdout.getvalue().strip().splitlines()
                self.assertEqual(output[-1], "X won!")

        # movements for victory O player by columns
        win_columns_movements = (
            ("2", "1", "5", "4", "9", "7"),
            ("1", "2", "4", "5", "6", "8"),
            ("7", "3", "8", "6", "2", "9"),
        )

        for i in range(3):
            with mock.patch("builtins.input", side_effect=win_columns_movements[i]):
                game = TicTacGame()
                game.start_game()
                output = sys.stdout.getvalue().strip().splitlines()
                self.assertEqual(output[-1], "O won!")

        # movements for draw
        draw_movements = (
            ("1", "3", "2", "4", "5", "8", "6", "9", "7"),
            ("1", "2", "3", "4", "6", "9", "7", "5", "8"),
        )

        for i in range(2):
            with mock.patch("builtins.input", side_effect=draw_movements[i]):
                game = TicTacGame()
                game.start_game()
                output = sys.stdout.getvalue().strip().splitlines()
                self.assertEqual(output[-1], "Draw!")


if __name__ == "__main__":
    unittest.main()
