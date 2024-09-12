import unittest
from unittest.mock import patch
from game.cli import Cli
from game.chess import Chess  

class TestCli(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '1', '2', '2'],)
    @patch('builtins.print')

    def test_play_happy(self,mock_print,mock_input):
        chess = Chess()
        cli = Cli()
        turn = chess.turn
        cli.play(chess)
        self.assertEqual(turn,"white")
        self.assertEqual(mock_input.call_count,4)
        self.assertEqual(mock_print.call_count,2)


    @patch('builtins.input', side_effect=['a','1', '1', '2', '2'])
    @patch('builtins.print')
    def test_play_sad(self, mock_print, mock_input):
        chess = Chess()
        cli = Cli()
        cli.play(chess)
        self.assertEqual(mock_input.call_count, 5)
        self.assertEqual(mock_print.call_count, 3)
        mock_print.assert_any_call("Entrada no válida. Por favor, introduce un número entre 0 y 7.")
        self.assertEqual(chess.turn, "black")


if __name__ == '__main__':
    unittest.main()