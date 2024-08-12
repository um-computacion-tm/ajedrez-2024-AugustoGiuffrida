import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../game')))

from game.board import Board
from game.cell import Cell

class TestBoard(unittest.TestCase):

    def test_create_board(self):
        board = Board().get_board()
        for row in range(8):
            for col in range(8):
                expected_color = "white" if (row + col) % 2 == 0 else "black"
                cell = board[row][col]
                self.assertIsInstance(cell, Cell, "Cada elemento del tablero debe ser una instancia de Cell.")
                self.assertEqual(cell.get_color(), expected_color, f"Celda en la posición {(row, col)} debería ser {expected_color}.")


    def test_initial_piece_placement(self):
            board = Board().get_board()
            # Verificar las piezas blancas
            self.assertEqual(str(board[7][0].get_piece()), 'r', "Debe haber una torre blanca en la posición a8.")
            self.assertEqual(str(board[7][1].get_piece()), 'h', "Debe haber un caballo blanco en la posición b8.")
            self.assertEqual(str(board[7][2].get_piece()), 'b', "Debe haber un alfil blanco en la posición c8.")
            self.assertEqual(str(board[7][3].get_piece()), 'q', "Debe haber una reina blanca en la posición d8.")
            self.assertEqual(str(board[7][4].get_piece()), 'k', "Debe haber un rey blanco en la posición e8.")
            self.assertEqual(str(board[7][5].get_piece()), 'b', "Debe haber un alfil blanco en la posición f8.")
            self.assertEqual(str(board[7][6].get_piece()), 'h', "Debe haber un caballo blanco en la posición g8.")
            self.assertEqual(str(board[7][7].get_piece()), 'r', "Debe haber una torre blanca en la posición h8.")
            # Verificar los peones blancos en la fila 7
            for col in range(8):
                self.assertEqual(str(board[6][col].get_piece()), 'p', f"Debe haber un peón blanco en la posición {chr(97 + col)}7.")
            # Verificar las piezas negras
            self.assertEqual(str(board[0][0].get_piece()), 'R', "Debe haber una torre negra en la posición a1.")
            self.assertEqual(str(board[0][1].get_piece()), 'H', "Debe haber un caballo negro en la posición b1.")
            self.assertEqual(str(board[0][2].get_piece()), 'B', "Debe haber un alfil negro en la posición c1.")
            self.assertEqual(str(board[0][3].get_piece()), 'Q', "Debe haber una reina negra en la posición d1.")
            self.assertEqual(str(board[0][4].get_piece()), 'K', "Debe haber un rey negro en la posición e1.")
            self.assertEqual(str(board[0][5].get_piece()), 'B', "Debe haber un alfil negro en la posición f1.")
            self.assertEqual(str(board[0][6].get_piece()), 'H', "Debe haber un caballo negro en la posición g1.")
            self.assertEqual(str(board[0][7].get_piece()), 'R', "Debe haber una torre negra en la posición h1.")
            # Verificar los peones negros en la fila 1
            for col in range(8):
                self.assertEqual(str(board[1][col].get_piece()), 'P', f"Debe haber un peón negro en la posición {chr(97 + col)}2.")


    def test_show_board_format(self):
        board_output = Board().show_board()
        lines = board_output.splitlines()
        self.assertEqual(len(lines), 19, "El tablero debe representarse en 19 líneas.")

        # Verificar las primeras y últimas líneas
        self.assertTrue(lines[0].startswith("    a     b     c     d     e     f     g     h"), "La primera línea del tablero no es correcta.")
        self.assertTrue(lines[-1].startswith("    a     b     c     d     e     f     g     h"), "La última línea del tablero no es correcta.")
        
        # Verificar algunas líneas centrales del tablero
        self.assertIn("  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘", lines, "La línea final del tablero no está presente.")
        self.assertIn("  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤", lines, "La línea de separación del tablero no está presente.")

if __name__ == "__main__":
    unittest.main()
