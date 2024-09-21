import unittest
from game.chess import Chess
from game.piece import Pawn, Rook, Knight, Bishop, Queen, King


class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_initial_turn(self):
        # Verifica que el turno inicial es "white"
        self.assertEqual(self.chess.turn, "white")

    def test_change_turn(self):
        # Cambia de turno y verifica que ahora es "black"
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "black")

        # Cambia de turno nuevamente y verifica que es "white"
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "white")

    def test_board_initialization(self):
        # Verifica que el tablero fue inicializado correctamente
        board = self.chess.board.get_positions()
        self.assertEqual(len(board), 8)
        self.assertEqual(len(board[0]), 8)

    def test_make_piece(self):
        # Verifica la creación de una pieza
        piece = self.chess.make_piece("pawn", "white", (6, 0))
        self.assertIsInstance(piece, Pawn)

        piece = self.chess.make_piece("rook", "black", (0, 0))
        self.assertIsInstance(piece, Rook)

        piece = self.chess.make_piece("knight", "white", (7, 1))
        self.assertIsInstance(piece, Knight)

        piece = self.chess.make_piece("bishop", "black", (0, 2))
        self.assertIsInstance(piece, Bishop)

        piece = self.chess.make_piece("queen", "white", (7, 3))
        self.assertIsInstance(piece, Queen)

        piece = self.chess.make_piece("king", "black", (0, 4))
        self.assertIsInstance(piece, King)


if __name__ == "__main__":
    unittest.main()