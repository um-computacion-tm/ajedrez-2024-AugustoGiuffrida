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

if __name__ == '__main__':
    unittest.main()
