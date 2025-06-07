import unittest
from oxo_logic import Game

class TestTicTacToe(unittest.TestCase):
    
    def setUp(self):
        self.game = Game()

    def test_initial_board_state(self):
        self.assertEqual(self.game.board, [" "] * 9)

    def test_user_move_valid(self):
        self.game.user_move(0)
        self.assertEqual(self.game.board[0], 'X')

    def test_user_move_invalid(self):
        self.game.user_move(0)
        with self.assertRaises(ValueError):
            self.game.user_move(0)

    def test_computer_move(self):
        result = self.game.computer_move()
        self.assertIn(result, ["", "O", "D"])

    def test_winning_move(self):
        self.game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(self.game._is_winning_move())

    def test_game_saving_and_restoring(self):
        self.game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', ' ', ' ']
        self.game.save_game()
        restored_game = Game.restore_game()
        self.assertEqual(restored_game.board, self.game.board)

if __name__ == "__main__":
    unittest.main()
