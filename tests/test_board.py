import unittest
from game.board import Board



class TestBoard(unittest.TestCase):

    def test_create_board(self):
        first_board = Board().create_board()  #Llama al método create_board() 
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
        expected_output = """  a b c d e f g h
8   *   *   *   * 8
7 *   *   *   *   7
6   *   *   *   * 6
5 *   *   *   *   5
4   *   *   *   * 4
3 *   *   *   *   3
2   *   *   *   * 2
1 *   *   *   *   1
  a b c d e f g h"""
        
        # Captura la salida del método show_board
        output = board.show_board()
        
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

##python3 -m unittest discover tests
        
        
