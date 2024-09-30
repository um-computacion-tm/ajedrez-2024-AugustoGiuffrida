import unittest
from game.piece import Pieces, Rook, Pawn, Bishop, Queen, King, Knight
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

class TestRook(unittest.TestCase):

    def test_valid_moves_horizontal(self):
        rook = Rook("white")
        rook_move = rook.valid_moves((0,0),(0,5))
        self.assertTrue(rook_move)

    def test_valid_moves_vertical(self):
        rook = Rook("black")
        rook_move = rook.valid_moves((0,0),(5,0))
        self.assertTrue(rook_move)

    def test_not_valid_moves_diagonal(self):
        rook = Rook("white")
        rook_move = rook.valid_moves((0,0),(1,1))
        self.assertFalse(rook_move)

    def test_not_valid_moves_same_position(self):
        rook = Rook("black")
        rook_move = rook.valid_moves((0,0),(0,0))
        self.assertFalse(rook_move)

class TestBishop(unittest.TestCase):

    def test_valid_moves_down_1(self):
        bishop = Bishop("white")
        bishop_move = bishop.valid_moves((0,0),(7,7))
        self.assertTrue(bishop_move)

    def test_valid_moves_down_2(self):
        bishop = Bishop("white")
        bishop_move = bishop.valid_moves((7,0),(0,7))
        self.assertTrue(bishop_move)

    def test_valid_moves_up_1(self):
        bishop = Bishop("black")
        bishop_move = bishop.valid_moves((7,7),(0,0))
        self.assertTrue(bishop_move)

    def test_valid_moves_up_1(self):
        bishop = Bishop("black")
        bishop_move = bishop.valid_moves((7,0),(0,7))
        self.assertTrue(bishop_move)

    def test_not_valid_moves_orthogonal(self):
        bishop = Bishop("white")
        bishop_move = bishop.valid_moves((0,0),(7,0))
        self.assertFalse(bishop_move)

    def test_not_valid_moves_same_position(self):
        bishop = Bishop("black")
        bishop_move = bishop.valid_moves((0,0),(0,0))
        self.assertFalse(bishop_move)                                    

class TestKnight(unittest.TestCase):

    def test_valid_moves_horizontal_1(self):
        knight = Knight("white")
        knight_move = knight.valid_moves((0,6),(1,4))
        self.assertTrue(knight_move)

    def test_valid_moves_horizontal_2(self):
        knight = Knight("white")
        knight_move = knight.valid_moves((0,1),(1,3))
        self.assertTrue(knight_move)        

    def test_valid_moves_vertical_1(self):
        knight = Knight("black")
        knight_move = knight.valid_moves((0,1),(2,2))
        self.assertTrue(knight_move)

    def test_valid_moves_vertical_2(self):
        knight = Knight("black")
        knight_move = knight.valid_moves((5,5),(3,4))
        self.assertTrue(knight_move)

    def test_not_valid_moves_diagonal(self):
        knight = Knight("white")
        knight_move = knight.valid_moves((0,0),(1,1))
        self.assertFalse(knight_move)

    def test_not_valid_moves_same_position(self):
        knight = Knight("black")
        knight_move = knight.valid_moves((0,0),(0,0))
        self.assertFalse(knight_move)

class TestKing(unittest.TestCase):

    def test_valid_moves_horizontal_1(self):
        king = King("white")
        king_move = king.valid_moves((0,0),(0,1))
        self.assertTrue(king_move)

    def test_valid_moves_horizontal_2(self):
        king = King("white")
        king_move = king.valid_moves((0,1),(0,0))
        self.assertTrue(king_move)        

    def test_valid_moves_vertical_1(self):
        king = King("black")
        king_move = king.valid_moves((5,5),(4,5))
        self.assertTrue(king_move)

    def test_valid_moves_vertical_2(self):
        king = King("black")
        king_move = king.valid_moves((5,5),(6,5))
        self.assertTrue(king_move)

    def test_valid_moves_diagonal_1(self):
        king = King("white")
        king_move = king.valid_moves((0,0),(1,1))
        self.assertTrue(king_move)

    def test_valid_moves_diagonal_2(self):
        king = King("white")
        king_move = king.valid_moves((1,1),(0,0))
        self.assertTrue(king_move)

    def test_not_valid_moves_(self):
        king = King("white")
        king_move = king.valid_moves((0,1),(2,2))
        self.assertFalse(king_move)

    def test_not_valid_moves_same_position(self):
        king = King("black")
        king_move = king.valid_moves((0,0),(0,0))
        self.assertFalse(king_move)

class TestQueen(unittest.TestCase):

    def test_valid_moves_horizontal_1(self):
        queen = Queen("white")
        queen_move = queen.valid_moves((0,0),(0,1))
        self.assertTrue(queen_move)

    def test_valid_moves_horizontal_2(self):
        queen = Queen("white")
        queen_move = queen.valid_moves((0,1),(0,0))
        self.assertTrue(queen_move)        

    def test_valid_moves_vertical_1(self):
        queen = Queen("black")
        queen_move = queen.valid_moves((5,5),(4,5))
        self.assertTrue(queen_move)

    def test_valid_moves_vertical_2(self):
        queen = Queen("black")
        queen_move = queen.valid_moves((5,5),(6,5))
        self.assertTrue(queen_move)

    def test_valid_moves_diagonal_1(self):
        queen = Queen("white")
        queen_move = queen.valid_moves((0,0),(1,1))
        self.assertTrue(queen_move)

    def test_valid_moves_diagonal_2(self):
        queen = Queen("white")
        queen_move = queen.valid_moves((1,1),(0,0))
        self.assertTrue(queen_move)

    def test_not_valid_moves_(self):
        queen = Queen("white")
        queen_move = queen.valid_moves((0,1),(2,2))
        self.assertFalse(queen_move)

    def test_not_valid_moves_same_position(self):
        queen = Queen("black")
        queen_move = queen.valid_moves((0,0),(0,0))
        self.assertFalse(queen_move)

if __name__ == '__main__':
    unittest.main()
