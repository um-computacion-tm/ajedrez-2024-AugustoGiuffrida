import unittest
from game.piece import Pieces, Rook, Pawn

class TestPieces(unittest.TestCase):

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
            piece.valid_moves(None)

if __name__ == '__main__':
    unittest.main()
