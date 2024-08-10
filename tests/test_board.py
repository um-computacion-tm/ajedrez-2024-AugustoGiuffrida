import unittest
import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from game.board import Board
from game.cell import Cell

class TestBoard(unittest.TestCase):

    def test_create_board(self):
        board = Board().create_board()
        for row in range(8):
            for col in range(8):
                expected_color = "white" if (row + col) % 2 == 0 else "black"
                cell = board[row][col]
                # Verificamos que el objeto sea una instancia de Cell
                self.assertIsInstance(cell, Cell)
                # Comparamos el color esperado con el color de la celda
                self.assertEqual(cell.get_color(), expected_color)
                # Comparamos el contenido de la celda
                self.assertEqual(cell.get_content(), " ")

    def test_show_board(self):
        # Generamos el tablero
        second_board = Board().show_board()

        # Ajustamos la salida esperada para que coincida con el formato de show_board
        second_output = """    a     b     c     d     e     f     g     h
  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
8 │  r  │  h  │  b  │  q  │  k  │  b  │  h  │  r  │ 8
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
7 │  p  │  p  │  p  │  p  │  p  │  p  │  p  │  p  │ 7
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
6 │     │     │     │     │     │     │     │     │ 6
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
5 │     │     │     │     │     │     │     │     │ 5
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
4 │     │     │     │     │     │     │     │     │ 4
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
3 │     │     │     │     │     │     │     │     │ 3
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
2 │  P  │  P  │  P  │  P  │  P  │  P  │  P  │  P  │ 2
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
1 │  R  │  H  │  B  │  Q  │  K  │  B  │  H  │  R  │ 1
  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
    a     b     c     d     e     f     g     h"""

        # Comparamos las cadenas directamente
        self.assertEqual(second_board.strip(), second_output.strip())

if __name__ == "__main__":
    unittest.main()
