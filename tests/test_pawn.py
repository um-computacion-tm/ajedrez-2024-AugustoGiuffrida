import unittest
from game.pawn import Pawn
from game.piece import Pieces

class TestPieces(unittest.TestCase):

    def test_pawn_initialization(self):
        pawn = Pawn("black", (1, 1))
        self.assertEqual(pawn.__color__, "black")
        self.assertEqual(pawn.__position__, (1, 1))
        self.assertEqual(pawn.__symbol__, "♟")

    def test_pawn_repr(self):
        pawn = Pawn("white", (6, 0))
        self.assertEqual(repr(pawn), "♙")

    def test_valid_moves_not_implemented(self):
        piece = Pieces("white", (0, 0))
        with self.assertRaises(NotImplementedError):
            piece.valid_moves(None)

if __name__ == '__main__':
    unittest.main()
