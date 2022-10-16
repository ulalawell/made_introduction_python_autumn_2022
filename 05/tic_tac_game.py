"""
Module with implementation of tic tac game
"""


class TicTacGame:
    """
    Implementation of tic tac game using class
    """

    def __init__(self):
        self.board = list(range(1, 10))

    def start_game(self):
        """
        Implementation of the method by which the game starts
        """
        move_number = 0

        while True:
            self.show_board()
            move_number += 1

            if move_number % 2 == 1:
                self.validate_input("X")
            else:
                self.validate_input("O")

            if move_number > 4:
                is_smb_won = self.check_winner()
                if is_smb_won:
                    print(is_smb_won, "won!")
                    break

            if move_number == 9:
                print("Draw!")
                break

    def show_board(self):
        """
        Implementation of the method showing the board
        """
        for i in range(3):
            print("-" * 13)
            print(
                "|",
                self.board[0 + i * 3],
                "|",
                self.board[1 + i * 3],
                "|",
                self.board[2 + i * 3],
                "|",
            )
        print("-" * 13)

    def validate_input(self, token):
        """
        Implementation of the method validating input
        """
        input_is_valid = False
        while not input_is_valid:
            player_answer = input("Where to put " + token + "?")

            if (
                player_answer.isdigit()
                and int(player_answer) >= 1
                and int(player_answer) <= 9
            ):
                if str(self.board[int(player_answer) - 1]) not in "XO":
                    self.board[int(player_answer) - 1] = token
                    input_is_valid = True
                else:
                    print("This cell is already taken")
            else:
                print("Incorrect input. Enter a number between 1 and 9 to make a move?")

    def check_winner(self):
        """
        Implementation of the method checking winner of the game
        """
        win_coordinates = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        )
        for coordinates in win_coordinates:
            if (
                self.board[coordinates[0]]
                == self.board[coordinates[1]]
                == self.board[coordinates[2]]
            ):
                return self.board[coordinates[0]]
        return False


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
