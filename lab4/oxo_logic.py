import os
import random
import oxo_data

class Game:
    def __init__(self):
        self.board = [" "] * 9

    def save_game(self):
        oxo_data.saveGame(self.board)

    @staticmethod
    def restore_game():
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                return Game.from_board(game)
            else:
                return Game()
        except IOError:
            return Game()

    @staticmethod
    def from_board(board):
        game = Game()
        game.board = board
        return game

    def _generate_move(self):
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        return random.choice(options) if options else -1

    def _is_winning_move(self):
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))

        for a, b, c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def user_move(self, cell):
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        self.board[cell] = 'X'
        return 'X' if self._is_winning_move() else ""

    def computer_move(self):
        cell = self._generate_move()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        return 'O' if self._is_winning_move() else ""

    def play(self):
        result = ""
        while not result:
            print(self.board)
            try:
                result = self.user_move(self._generate_move())
            except ValueError:
                print("Oops, that shouldn't happen")
            if not result:
                result = self.computer_move()

            if result:
                print("Its a draw" if result == 'D' else f"Winner is: {result}")
            print(self.board)

if __name__ == "__main__":
    game = Game()
    game.play()


            