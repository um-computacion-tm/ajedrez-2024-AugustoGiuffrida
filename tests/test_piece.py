import unittest
from game.piece import Pieces

class TestPieces(unittest.TestCase):

    def test_piece_initialization(self):
        piece = Pieces("white", (0, 0))
        self.assertEqual(piece.__color__, "white")
        self.assertEqual(piece.__position__, (0, 0))
        self.assertIsNone(piece.__symbol__)

    def test_piece_move(self):
        piece = Pieces("black", (1, 1))
        piece.move((2, 2))
        self.assertEqual(piece.__position__, (2, 2))

    def test_piece_repr_without_symbol(self):
        piece = Pieces("white", (0, 0))
        self.assertEqual(repr(piece), "?")

    def test_valid_moves_not_implemented(self):
        piece = Pieces("white", (0, 0))
        with self.assertRaises(NotImplementedError):
            piece.valid_moves(None)

if __name__ == '__main__':
    unittest.main()