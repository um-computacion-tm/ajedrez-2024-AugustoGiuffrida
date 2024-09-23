import unittest
from game.piece import Pieces, Rook, Pawn
from game.chess import Chess
from game.board import Board
from game.cell import Cell


class TestPieces(unittest.TestCase):

    def setUp(self):
        self.board = [[Cell("white", (i, j)) for j in range(8)] for i in range(8)]
        self.pawn = Pawn("white")
        self.rook = Rook("white")

    def test_piece_initialization(self):
        piece = Pieces("white")
        self.assertEqual(piece.get_color(), "white")

    

    # def test_get_color_1(self):
    #     board = Board()  
    #     piece = board.__positions__[7][2]  
    #     self.assertEqual(piece.get_color(), "white")  

    # def test_get_color_2(self):
    #     board = Board()  
    #     piece = board.__positions__[0][0]  
    #     self.assertEqual(piece.get_color(), "black") 

if __name__ == '__main__':
    unittest.main()
