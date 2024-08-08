import unittest
import sys
import os

# Asegúrate de que la ruta del directorio del proyecto esté en sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.board import Board

class TestBoard(unittest.TestCase):

    def test_create_board(self):
        first_board = Board().create_board()  # Llama al método create_board() 
        first_output = [
            [" ", "*", " ", "*", " ", "*", " ", "*"],
            ["*", " ", "*", " ", "*", " ", "*", " "],
            [" ", "*", " ", "*", " ", "*", " ", "*"],
            ["*", " ", "*", " ", "*", " ", "*", " "],
            [" ", "*", " ", "*", " ", "*", " ", "*"],
            ["*", " ", "*", " ", "*", " ", "*", " "],
            [" ", "*", " ", "*", " ", "*", " ", "*"],
            ["*", " ", "*", " ", "*", " ", "*", " "]
        ]
        self.assertEqual(first_board, first_output)

    def test_show_board(self):
        board = Board()
        expected_output = """     a     b     c     d     e     f     g     h
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
        
        # Captura la salida del método show_board
        output = board.show_board()

if __name__ == '__main__':
    unittest.main()

##python3 -m unittest discover tests
        
        
