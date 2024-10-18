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

    def setUp(self):
        self.board = Board()

    def test_valid_moves_horizontal(self):
        rook = Rook("white")
        rook_move = rook.valid_moves((0,0),(0,5),self.board)
        self.assertTrue(rook_move)

    def test_valid_moves_vertical(self):
        rook = Rook("black")
        rook_move = rook.valid_moves((0,0),(5,0),self.board)
        self.assertTrue(rook_move)

    def test_not_valid_moves_diagonal(self):
        rook = Rook("white")
        rook_move = rook.valid_moves((0,0),(1,1),self.board)
        self.assertFalse(rook_move)

    def test_not_valid_moves_same_position(self):
        rook = Rook("black")
        rook_move = rook.valid_moves((0,0),(0,0),self.board)
        self.assertFalse(rook_move)

class TestBishop(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_valid_moves_down_1(self):
        bishop = Bishop("white")
        bishop_move = bishop.valid_moves((0,0),(7,7),self.board)
        self.assertTrue(bishop_move)

    def test_valid_moves_down_2(self):
        bishop = Bishop("white")
        bishop_move = bishop.valid_moves((7,0),(0,7),self.board)
        self.assertTrue(bishop_move)

    def test_valid_moves_up_1(self):
        bishop = Bishop("black")
        bishop_move = bishop.valid_moves((7,7),(0,0),self.board)
        self.assertTrue(bishop_move)

    def test_valid_moves_up_1(self):
        bishop = Bishop("black")
        bishop_move = bishop.valid_moves((7,0),(0,7),self.board)
        self.assertTrue(bishop_move)

    def test_not_valid_moves_orthogonal(self):
        bishop = Bishop("white")
        bishop_move = bishop.valid_moves((0,0),(7,0),self.board)
        self.assertFalse(bishop_move)

    def test_not_valid_moves_same_position(self):
        bishop = Bishop("black")
        bishop_move = bishop.valid_moves((0,0),(0,0),self.board)
        self.assertFalse(bishop_move)                                    

import unittest

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_valid_move_one_step_forward_white(self):
        pawn = Pawn("white")
        pawn_move = pawn.valid_moves((1, 0), (2, 0), self.board)
        self.assertTrue(pawn_move)

    def test_valid_move_one_step_forward_black(self):
        pawn = Pawn("black")
        pawn_move = pawn.valid_moves((6, 0), (5, 0), self.board)
        self.assertTrue(pawn_move)

    def test_valid_move_two_steps_forward_white(self):
        pawn = Pawn("white")
        pawn_move = pawn.valid_moves((1, 0), (3, 0), self.board)
        self.assertTrue(pawn_move)

    def test_valid_move_two_steps_forward_black(self):
        pawn = Pawn("black")
        pawn_move = pawn.valid_moves((6, 0), (4, 0), self.board)
        self.assertTrue(pawn_move)

    def test_not_valid_move_three_steps_forward(self):
        pawn = Pawn("white")
        pawn_move = pawn.valid_moves((1, 0), (4, 0), self.board)
        self.assertFalse(pawn_move)

    def test_valid_diagonal_capture_white(self):
        pawn = Pawn("white")
        enemy_pawn = Pawn("black")
        source = (1, 0)  # Posición inicial del peón blanco
        dest = (2, 1)    # Destino donde se quiere capturar

        # Colocar el peón blanco en la posición de origen
        self.board.get_cell(source[0], source[1]).place_piece(pawn)
        # Colocar el peón negro en la posición de destino para que sea capturado
        self.board.get_cell(dest[0], dest[1]).place_piece(enemy_pawn)

        # Ejecutar el movimiento
        pawn_move = pawn.valid_moves(source, dest, self.board)
        self.assertTrue(pawn_move)  # Verificar que el movimiento es válido

    def test_valid_diagonal_capture_black(self):
        pawn = Pawn("black")
        enemy_pawn = Pawn("white")
        source = (2, 1)  # Posición inicial del peón negro
        dest = (1, 0)    # Destino donde se quiere capturar

        # Colocar el peón negro en la posición de origen
        self.board.get_cell(source[0], source[1]).place_piece(pawn)
        # Colocar el peón blanco en la posición de destino para que sea capturado
        self.board.get_cell(dest[0], dest[1]).place_piece(enemy_pawn)

        # Ejecutar el movimiento
        pawn_move = pawn.valid_moves(source, dest, self.board)
        self.assertTrue(pawn_move)  # Verificar que el movimiento es válido

    def test_not_valid_diagonal_move_without_capture(self):
        pawn = Pawn("white")
        pawn_move = pawn.valid_moves((1, 0), (2, 1), self.board)
        self.assertFalse(pawn_move)

    def test_not_valid_move_backward(self):
        pawn = Pawn("white")
        pawn_move = pawn.valid_moves((3, 0), (2, 0), self.board)
        self.assertFalse(pawn_move)

    def test_not_valid_move_same_position(self):
        pawn = Pawn("black")
        pawn_move = pawn.valid_moves((6, 0), (6, 0), self.board)
        self.assertFalse(pawn_move)



class TestKnight(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_valid_moves_horizontal_1(self):
        knight = Knight("white")
        knight_move = knight.valid_moves((0,6),(1,4),self.board)
        self.assertTrue(knight_move)

    def test_valid_moves_horizontal_2(self):
        knight = Knight("white")
        knight_move = knight.valid_moves((0,1),(1,3),self.board)
        self.assertTrue(knight_move)        

    def test_valid_moves_vertical_1(self):
        knight = Knight("black")
        knight_move = knight.valid_moves((0,1),(2,2),self.board)
        self.assertTrue(knight_move)

    def test_valid_moves_vertical_2(self):
        knight = Knight("black")
        knight_move = knight.valid_moves((5,5),(3,4),self.board)
        self.assertTrue(knight_move)

    def test_not_valid_moves_diagonal(self):
        knight = Knight("white")
        knight_move = knight.valid_moves((0,0),(1,1),self.board)
        self.assertFalse(knight_move)

    def test_not_valid_moves_same_position(self):
        knight = Knight("black")
        knight_move = knight.valid_moves((0,0),(0,0),self.board)
        self.assertFalse(knight_move)

class TestKing(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_valid_moves_horizontal_1(self):
        king = King("white")
        king_move = king.valid_moves((0,0),(0,1),self.board)
        self.assertTrue(king_move)

    def test_valid_moves_horizontal_2(self):
        king = King("white")
        king_move = king.valid_moves((0,1),(0,0),self.board)
        self.assertTrue(king_move)        

    def test_valid_moves_vertical_1(self):
        king = King("black")
        king_move = king.valid_moves((5,5),(4,5),self.board)
        self.assertTrue(king_move)

    def test_valid_moves_vertical_2(self):
        king = King("black")
        king_move = king.valid_moves((5,5),(6,5),self.board)
        self.assertTrue(king_move)

    def test_valid_moves_diagonal_1(self):
        king = King("white")
        king_move = king.valid_moves((0,0),(1,1),self.board)
        self.assertTrue(king_move)

    def test_valid_moves_diagonal_2(self):
        king = King("white")
        king_move = king.valid_moves((1,1),(0,0),self.board)
        self.assertTrue(king_move)

    def test_not_valid_moves_(self):
        king = King("white")
        king_move = king.valid_moves((0,1),(2,2),self.board)
        self.assertFalse(king_move)

    def test_not_valid_moves_same_position(self):
        king = King("black")
        king_move = king.valid_moves((0,0),(0,0),self.board)
        self.assertFalse(king_move)

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_valid_moves_horizontal_1(self):
        queen = Queen("white")
        queen_move = queen.valid_moves((0,0),(0,1),self.board)
        self.assertTrue(queen_move)

    def test_valid_moves_horizontal_2(self):
        queen = Queen("white")
        queen_move = queen.valid_moves((0,1),(0,0),self.board)
        self.assertTrue(queen_move)        

    def test_valid_moves_vertical_1(self):
        queen = Queen("black")
        queen_move = queen.valid_moves((5,5),(4,5),self.board)
        self.assertTrue(queen_move)

    def test_valid_moves_vertical_2(self):
        queen = Queen("black")
        queen_move = queen.valid_moves((5,5),(6,5),self.board)
        self.assertTrue(queen_move)

    def test_valid_moves_diagonal_1(self):
        queen = Queen("white")
        queen_move = queen.valid_moves((0,0),(1,1),self.board)
        self.assertTrue(queen_move)

    def test_valid_moves_diagonal_2(self):
        queen = Queen("white")
        queen_move = queen.valid_moves((1,1),(0,0),self.board)
        self.assertTrue(queen_move)

    def test_not_valid_moves_(self):
        queen = Queen("white")
        queen_move = queen.valid_moves((0,1),(2,2),self.board)
        self.assertFalse(queen_move)

    def test_not_valid_moves_same_position(self):
        queen = Queen("black")
        queen_move = queen.valid_moves((0,0),(0,0),self.board)
        self.assertFalse(queen_move)

if __name__ == '__main__':
    unittest.main()
