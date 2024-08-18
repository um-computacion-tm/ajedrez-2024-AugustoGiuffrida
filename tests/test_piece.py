import unittest
from game.piece import Pieces, Rook, Pawn
from game.cell import Cell

class TestPieces(unittest.TestCase):

    def setUp(self):
        self.board = [[Cell("white", (i, j)) for j in range(8)] for i in range(8)]
        self.rook = Rook("white", (4, 4))
        self.pawn = Pawn("white", (6, 0))

    def test_piece_initialization(self):
        piece = Pieces("white", (0, 0))
        self.assertEqual(piece.get_color(), "white")
        self.assertEqual(piece.get_position(), (0, 0))
        self.assertIsNone(piece.get_symbol())

    def test_piece_repr_without_symbol(self):
        piece = Pieces("white", (0, 0))
        self.assertEqual(repr(piece), "")

    def test_valid_moves_not_implemented(self):
        piece = Pieces("white", (0, 0))
        with self.assertRaises(NotImplementedError):
            piece.valid_moves(self.board)

    def test_rook_valid_moves_vertical(self):
        moves = self.rook.valid_moves_vertical(self.board)
        expected_moves = [(3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4)]
        self.assertEqual(moves, expected_moves)

    def test_rook_valid_moves_horizontal(self):
        moves = self.rook.valid_moves_horizontal(self.board)
        expected_moves = [(4, 3), (4, 2), (4, 1), (4, 0), (4, 5), (4, 6), (4, 7)]
        self.assertEqual(moves, expected_moves)

    def test_pawn_valid_moves_initial_position(self):
        moves = self.pawn.valid_moves(self.board)
        expected_moves = [(5, 0), (4, 0)]
        self.assertEqual(moves, expected_moves)

    def test_pawn_valid_moves_after_move(self):
        self.pawn.move((5, 0), self.board)
        moves = self.pawn.valid_moves(self.board)
        expected_moves = [(4, 0)]
        self.assertEqual(moves, expected_moves)

    def test_pawn_cannot_move_forward_if_blocked(self):
        self.board[5][0].place_piece(Pawn("black", (5, 0)))
        moves = self.pawn.valid_moves(self.board)
        self.assertEqual(moves, [])

if __name__ == '__main__':
    unittest.main()
