import unittest
from game.piece import Pieces, Rook, Pawn

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

    def test_rook_initialization(self):
        rook = Rook("white", (0, 0))
        self.assertEqual(rook.__color__, "white")
        self.assertEqual(rook.__position__, (0, 0))
        self.assertEqual(rook.__symbol__, "♖")

    def test_rook_repr(self):
        rook = Rook("black", (7, 7))
        self.assertEqual(repr(rook), "♜")

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