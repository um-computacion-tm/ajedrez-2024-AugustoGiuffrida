import unittest
from game.rook import Rook
from game.piece import Pieces

class TestPieces(unittest.TestCase):

    def test_rook_initialization(self):
        rook = Rook("white", (0, 0))
        self.assertEqual(rook.__color__, "white")
        self.assertEqual(rook.__position__, (0, 0))
        self.assertEqual(rook.__symbol__, "♖")

    def test_rook_repr(self):
        rook = Rook("black", (7, 7))
        self.assertEqual(repr(rook), "♜")

    def test_valid_moves_not_implemented(self):
        piece = Pieces("white", (0, 0))
        with self.assertRaises(NotImplementedError):
            piece.valid_moves(None)
if __name__ == '__main__':
    unittest.main()