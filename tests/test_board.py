import unittest
from unittest.mock import patch, MagicMock
from game.board import Board
from game.cell import Cell


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
    

    # def test_show_board_format(self):
    #     board_output = Board().show_board()
    #     lines = board_output.splitlines()
    #     self.assertEqual(len(lines), 19, "El tablero debe representarse en 19 líneas.")

    #     # Verificar las primeras y últimas líneas
    #     self.assertTrue(lines[0].startswith("                                               a      b        c       d       e       f       g       h"), "La primera línea del tablero no es correcta.")
    #     self.assertTrue(lines[-1].startswith("                                               a      b        c       d       e       f       g       h"), "La última línea del tablero no es correcta.")
        
    #     # Verificar algunas líneas centrales del tablero
    #     self.assertIn("                                           └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘", lines, "La línea final del tablero no está presente.")
    #     self.assertIn("                                           ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤", lines, "La línea de separación del tablero no está presente.")

if __name__ == "__main__":
    unittest.main()
