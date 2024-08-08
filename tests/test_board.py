import unittest


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
                self.assertEqual(cell.color, expected_color)
                # Comparamos el contenido de la celda
                self.assertEqual(cell.content, " ")


    def test_show_board(self):
        second_board = Board().show_board()
        second_output = """     a     b     c     d     e     f     g     h
  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
8 │     │  *  │     │  *  │     │  *  │     │  *  │ 8
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
7 │  *  │     │  *  │     │  *  │     │  *  │     │ 7
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
6 │     │  *  │     │  *  │     │  *  │     │  *  │ 6
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
5 │  *  │     │  *  │     │  *  │     │  *  │     │ 5
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
4 │     │  *  │     │  *  │     │  *  │     │  *  │ 4
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
3 │  *  │     │  *  │     │  *  │     │  *  │     │ 3
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
2 │     │  *  │     │  *  │     │  *  │     │  *  │ 2
  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
1 │  *  │     │  *  │     │  *  │     │  *  │     │ 1
  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
     a     b     c     d     e     f     g     h"""
        
        normalized_board = "\n".join([line.strip() for line in second_board.splitlines()])
        normalized_output = "\n".join([line.strip() for line in second_output.splitlines()])

        self.assertEqual(normalized_board, normalized_output)




        
