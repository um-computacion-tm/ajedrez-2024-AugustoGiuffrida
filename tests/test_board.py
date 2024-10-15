import unittest
from unittest.mock import patch, MagicMock
from game.board import Board
from game.cell import Cell
from game.piece import Rook,Pawn,Bishop,Queen,King,Knight


class TestBoard(unittest.TestCase):

    def test_create_board(self):
        board = Board().get_positions()
        for row in range(8):
            for col in range(8):
                expected_color = "white" if (row + col) % 2 == 0 else "black"
                cell = board[row][col]
                self.assertIsInstance(cell, Cell, "Cada elemento del tablero debe ser una instancia de Cell.")
                self.assertEqual(cell.get_color(), expected_color, f"Celda en la posición {(row, col)} debería ser {expected_color}.")

    def test_get_positions_matrix(self):
        positions = Board().get_positions()
        self.assertEqual(len(positions),8)

    def test_get_positions_elements_1(self):
        positions = Board().get_positions()
        cell = positions[2][0]
        self.assertEqual(len(positions[2]),8)
        self.assertEqual(len(positions[0]),8)
        self.assertIsInstance(cell,Cell)

    def test_get_positions_elements_2(self):
        positions = Board().get_positions()
        cell = positions[5][4]
        self.assertEqual(len(positions[5]),8)
        self.assertEqual(len(positions[4]),8)
        self.assertIsInstance(cell,Cell)

    def test_get_positions_elements_3(self):
        positions = Board().get_positions()
        cell = positions[7][7]
        self.assertEqual(len(positions[7]),8)
        self.assertEqual(len(positions[7]),8)
        self.assertIsInstance(cell,Cell)

###### Tests orthogonal_move ######

    def test_orthogonal_move_horizontal_no_obstacle(self):
        board = Board()
        source = (0,0)
        dest = (0,3)

        for i in range (1,3):
            board.__positions__[0][i].is_occupied = MagicMock(return_value=False)            

        result = board.orthogonal_move(source, dest)

        self.assertTrue(result)

    def test_orthogonal_move_horizontal_with_obstacle(self):
        board = Board()
        source = (0,0)
        dest = (0,3)

        board.__positions__[0][2].is_occupied = MagicMock(return_value=True)            

        result = board.orthogonal_move(source, dest)

        self.assertFalse(result)

    def test_orthogonal_move_horizontal_with_obstacles(self):
        board = Board()
        source = (0,0)
        dest = (0,3)

        for i in range (1,3):
            board.__positions__[0][i].is_occupied = MagicMock(return_value=True)            

        result = board.orthogonal_move(source, dest)

        self.assertFalse(result)

    def test_orthogonal_move_vertical_no_obstacle(self):
        board = Board()
        source = (0,0)
        dest = (3,0)

        for i in range (1,3):
            board.__positions__[i][0].is_occupied = MagicMock(return_value=False)            

        result = board.orthogonal_move(source, dest)

        self.assertTrue(result)

    def test_orthogonal_move_vertical_with_obstacle(self):
        board = Board()
        source = (0,0)
        dest = (3,0)

        board.__positions__[2][0].is_occupied = MagicMock(return_value=True)            

        result = board.orthogonal_move(source, dest)

        self.assertFalse(result)

    def test_orthogonal_move_vertical_with_obstacles(self):
        board = Board()
        source = (0,0)
        dest = (3,0)

        for i in range (1,3):
            board.__positions__[i][0].is_occupied = MagicMock(return_value=True)            

        result = board.orthogonal_move(source, dest)

        self.assertFalse(result)
    
###### Tests diagonal_move ######

    def test_diagonal_move_down_no_obstacle_1(self):
        board = Board()
        source = (0, 0)
        dest = (7, 7)

        for i in range(1, 7):
            board.__positions__[i][i].is_occupied = MagicMock(return_value=False)            

        result = board.diagonal_move(source, dest)
        self.assertTrue(result)

    def test_diagonal_move_down_no_obstacle_2(self):
        board = Board()
        source = (0, 7)
        dest = (7, 0)

        for i in range(1, 7):
            board.__positions__[i][7 - i].is_occupied = MagicMock(return_value=False)            

        result = board.diagonal_move(source, dest)
        self.assertTrue(result)

    def test_diagonal_move_up_no_obstacle_1(self):
        board = Board()
        source = (7, 7)
        dest = (0, 0)

        for i in range(1, 7):
            board.__positions__[7 - i][7 - i].is_occupied = MagicMock(return_value=False)            

        result = board.diagonal_move(source, dest)
        self.assertTrue(result)

    def test_diagonal_move_up_no_obstacle_2(self):
        board = Board()
        source = (7, 0)
        dest = (0, 7)

        for i in range(1, 7):
            board.__positions__[7 - i][i].is_occupied = MagicMock(return_value=False)            

        result = board.diagonal_move(source, dest)
        self.assertTrue(result)

    def test_diagonal_move_with_obstacle(self):
        board = Board()
        source = (0, 0)
        dest = (3, 3)

        board.__positions__[2][2].is_occupied = MagicMock(return_value=True)            

        result = board.diagonal_move(source, dest)
        self.assertFalse(result)

    def test_diagonal_move_with_multiple_obstacles(self):
        board = Board()
        source = (7, 7)
        dest = (0, 0)

        for i in range(1, 7):
            board.__positions__[7 - i][7 - i].is_occupied = MagicMock(return_value=True)            

        result = board.diagonal_move(source, dest)
        self.assertFalse(result)

###Peon###

    def tests_check_path_pawn_valid(self):
        source = (1,1)
        dest = (3,1)
        board = Board()
        pawn = Pawn("white")

        board.__positions__[source[0]][source[1]].place_piece(pawn)
        pawn.valid_moves = MagicMock(return_value=True)

        result = board.check_path(pawn, source, dest)

        self.assertTrue(result)

    def tests_check_path_pawn_capture(self):
        source = (1,1)
        dest = (2,2)
        board = Board()
        pawn = Pawn("white")
        enemy_pawn = Pawn("black")

        board.__positions__[source[0]][source[1]].place_piece(pawn)
        board.__positions__[dest[0]][dest[1]].place_piece(enemy_pawn)
        pawn.valid_moves = MagicMock(return_value=True)

        result = board.check_path(pawn, source, dest)

        self.assertTrue(result)

    def tests_check_path_pawn_invalid(self):
        source = (1,1)
        dest = (2,2)
        board = Board()
        pawn = Pawn("white")

        board.__positions__[source[0]][source[1]].place_piece(pawn)
        pawn.valid_moves = MagicMock(return_value=False)

        result = board.check_path(pawn, source, dest)

        self.assertFalse(result)

###Torre

    def tests_check_path_rook_valid(self):
        source = (0,0)
        dest = (0,7)
        board = Board()
        rook = Rook("white")

        board.__positions__[source[0]][source[1]].place_piece(rook)
        board.orthogonal_move = MagicMock(return_value=True)

        result = board.check_path(rook, source, dest)

        self.assertTrue(result)

    def tests_check_path_rook_capture(self):
        source = (0,0)
        dest = (0,7)
        board = Board()
        rook = Rook("white")
        enemy_rook = Rook("black")

        board.__positions__[source[0]][source[1]].place_piece(rook)
        board.__positions__[dest[0]][dest[1]].place_piece(enemy_rook)
        board.orthogonal_move = MagicMock(return_value=True)

        result = board.check_path(rook, source, dest)

        self.assertTrue(result)

    def tests_check_path_rook_invalid(self):
        source = (0,0)
        dest = (7,7)
        board = Board()
        rook = Rook("white")

        board.__positions__[source[0]][source[1]].place_piece(rook)
        board.orthogonal_move = MagicMock(return_value=False)

        result = board.check_path(rook, source, dest)

        self.assertFalse(result)    

###Caballo###

    def tests_check_path_knight_valid(self):
        source = (0,1)
        dest = (2,2)
        board = Board()
        knight = Knight("white")

        board.__positions__[source[0]][source[1]].place_piece(knight)
        knight.valid_moves = MagicMock(return_value=True)

        result = board.check_path(knight, source, dest)

        self.assertTrue(result)

    def tests_check_path_knight_capture(self):
        source = (0,1)
        dest = (2,2)
        board = Board()
        knight = Knight("white")
        enemy_knight = Knight("black")

        board.__positions__[source[0]][source[1]].place_piece(knight)
        board.__positions__[dest[0]][dest[1]].place_piece(enemy_knight)
        knight.valid_moves = MagicMock(return_value=True)

        result = board.check_path(knight, source, dest)

        self.assertTrue(result)

    def tests_check_path_knight_invalid(self):
        source = (0,1)
        dest = (7,1)
        board = Board()
        knight = Knight("white")

        board.__positions__[source[0]][source[1]].place_piece(knight)
        knight.valid_moves = MagicMock(return_value=False)

        result = board.check_path(knight, source, dest)

        self.assertFalse(result)

###Alfil###

    def tests_check_path_bishop_valid(self):
        source = (0,0)
        dest = (7,7)
        board = Board()
        bishop = Bishop("white")

        board.__positions__[source[0]][source[1]].place_piece(bishop)
        board.diagonal_move = MagicMock(return_value=True)

        result = board.check_path(bishop, source, dest)

        self.assertTrue(result)

    def tests_check_path_bishop_capture(self):
        source = (0,0)
        dest = (7,7)
        board = Board()
        bishop = Bishop("white")
        enemy_bishop = Bishop("black")

        board.__positions__[source[0]][source[1]].place_piece(bishop)
        board.__positions__[dest[0]][dest[1]].place_piece(enemy_bishop)
        board.diagonal_move = MagicMock(return_value=True)

        result = board.check_path(bishop, source, dest)

        self.assertTrue(result)

    def tests_check_path_bishop_invalid(self):
        source = (0,0)
        dest = (7,0)
        board = Board()
        bishop = Bishop("white")

        board.__positions__[source[0]][source[1]].place_piece(bishop)
        board.diagonal_move = MagicMock(return_value=False)

        result = board.check_path(bishop, source, dest)

        self.assertFalse(result)

###Rey###

    def tests_check_path_king_valid_diagonal(self):
        source = (0,4)
        dest = (1,5)
        board = Board()
        king = King("white")

        board.__positions__[source[0]][source[1]].place_piece(king)
        board.diagonal_move = MagicMock(return_value=True)

        result = board.check_path(king, source, dest)

        self.assertTrue(result)

    def tests_check_path_king_valid_orthogonal(self):
        source = (0,4)
        dest = (0,5)
        board = Board()
        king = King("white")

        board.__positions__[source[0]][source[1]].place_piece(king)
        board.orthogonal_move = MagicMock(return_value=True)

        result = board.check_path(king, source, dest)

        self.assertTrue(result)

    def tests_check_path_king_diagonal_capture(self):
        source = (0,4)
        dest = (1,5)
        board = Board()
        king = King("white")
        enemy_king = King("black")

        board.__positions__[source[0]][source[1]].place_piece(king)
        board.diagonal_move = MagicMock(return_value=True)
        board.__positions__[dest[0]][dest[1]].place_piece(enemy_king)

        result = board.check_path(king, source, dest)

        self.assertTrue(result)

    def tests_check_path_king_orthogonal_capture(self):
        source = (0,4)
        dest = (0,5)
        board = Board()
        king = King("white")
        enemy_king = King("black")

        board.__positions__[source[0]][source[1]].place_piece(king)
        board.orthogonal_move = MagicMock(return_value=True)
        board.__positions__[dest[0]][dest[1]].place_piece(enemy_king)

        result = board.check_path(king, source, dest)

        self.assertTrue(result)

    def tests_check_path_king_invalid(self):
        source = (0,4)
        dest = (0,7)
        board = Board()
        king = King("white")

        board.__positions__[source[0]][source[1]].place_piece(king)
        board.orthogonal_move = MagicMock(return_value=False)

        result = board.check_path(king, source, dest)

        self.assertFalse(result)

###Reina####

    def tests_check_path_queen_valid_diagonal(self):
        source = (0,0)
        dest = (7,7)
        board = Board()
        queen = Queen("white")

        board.__positions__[source[0]][source[1]].place_piece(queen)
        board.diagonal_move = MagicMock(return_value=True)

        result = board.check_path(queen, source, dest)

        self.assertTrue(result)

    def tests_check_path_king_queen_orthogonal(self):
        source = (0,0)
        dest = (0,7)
        board = Board()
        queen = Queen("white")

        board.__positions__[source[0]][source[1]].place_piece(queen)
        board.orthogonal_move = MagicMock(return_value=True)

        result = board.check_path(queen, source, dest)

        self.assertTrue(result)

    def tests_check_path_queen_diagonal_capture(self):
        source = (0,0)
        dest = (7,7)
        board = Board()
        queen = Queen("white")
        enemy_queen = Queen("black")

        board.__positions__[source[0]][source[1]].place_piece(queen)
        board.diagonal_move = MagicMock(return_value=True)
        board.__positions__[dest[0]][dest[1]].place_piece(enemy_queen)

        result = board.check_path(queen, source, dest)

        self.assertTrue(result)

    def tests_check_path_queen_orthogonal_capture(self):
        source = (0,0)
        dest = (0,7)
        board = Board()
        queen = Queen("white")
        enemy_queen = Queen("black")

        board.__positions__[source[0]][source[1]].place_piece(queen)
        board.orthogonal_move = MagicMock(return_value=True)
        board.__positions__[dest[0]][dest[1]].place_piece(enemy_queen)

        result = board.check_path(queen, source, dest)

        self.assertTrue(result)

    def tests_check_path_queen_invalid(self):
        source = (0,1)
        dest = (2,2)
        board = Board()
        queen = Queen("white")

        board.__positions__[source[0]][source[1]].place_piece(queen)
        board.orthogonal_move = MagicMock(return_value=False)

        result = board.check_path(queen, source, dest)

        self.assertFalse(result)

####### Tests is_valid ######

    def test_is_valid_move_empty_destination(self):
        source = (1, 1)
        dest =  (7, 7)

        board = Board()

        piece = Rook("white")
        board.__positions__[source[0]][source[1]].place_piece(piece)


        cell = board.__positions__[source[0]][source[1]]
        piece = cell.get_piece()
        piece.valid_moves = MagicMock(return_value=True)

        dest_cell = board.__positions__[dest[0]][dest[1]]
        dest_cell.is_occupied = MagicMock(return_value=False)

        result = board.is_valid(source,dest)

        self.assertTrue(result) 

    def test_is_valid_move_capture(self):
        source = (1, 1)
        dest =  (7, 7)

        board = Board()

        piece = Rook("white")
        board.__positions__[source[0]][source[1]].place_piece(piece)

        friendly_piece = Rook("black")
        board.__positions__[dest[0]][dest[1]].place_piece(friendly_piece)

        cell = board.__positions__[source[0]][source[1]]
        piece = cell.get_piece()
        piece.valid_moves = MagicMock(return_value=True)

        dest_cell = board.__positions__[dest[0]][dest[1]]
        dest_cell.is_occupied = MagicMock(return_value=True)

        #Preguntarle al elio si esto necesario
        board.check_path = MagicMock(return_value=True)

        result = board.is_valid(source,dest)

        self.assertTrue(result)

    def test_is_valid_move_same_color(self):
        source = (1, 1)
        dest =  (7, 7)

        board = Board()

        piece = Rook("white")
        board.__positions__[source[0]][source[1]].place_piece(piece)

        friendly_piece = Rook("white")
        board.__positions__[dest[0]][dest[1]].place_piece(friendly_piece)

        cell = board.__positions__[source[0]][source[1]]
        piece = cell.get_piece()
        piece.valid_moves = MagicMock(return_value=True)

        dest_cell = board.__positions__[dest[0]][dest[1]]
        dest_cell.is_occupied = MagicMock(return_value=True)

        #Preguntarle al elio si esto necesario
        board.check_path = MagicMock(return_value=True)

        result = board.is_valid(source,dest)

        self.assertFalse(result)  


    # def test_show_board_format(self):
    #     board_output = Board().show_board()
    #     lines = board_output.splitlines()
    #     self.assertEqual(len(lines), 19, "El tablero debe representarse en 19 líneas.")

    #     # Verificar las primeras y últimas líneas
    #     self.assertTrue(lines[0].startswith("    a     b     c     d     e     f     g     h"), "La primera línea del tablero no es correcta.")
    #     self.assertTrue(lines[-1].startswith("    a     b     c     d     e     f     g     h"), "La última línea del tablero no es correcta.")
        
    #     # Verificar algunas líneas centrales del tablero
    #     self.assertIn("  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘", lines, "La línea final del tablero no está presente.")
    #     self.assertIn("  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤", lines, "La línea de separación del tablero no está presente.")

if __name__ == "__main__":
    unittest.main()
