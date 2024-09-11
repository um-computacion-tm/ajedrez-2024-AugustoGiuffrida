import unittest
from unittest.mock import patch
from game.cli import Cli
from game.chess import Chess  

class TestCli(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '1', '2', '2'],)
    @patch('builtins.print')

    def test_play(self,mock_print,mock_input):
        chess = Chess()
        cli = Cli()
        turn = chess.turn
        cli.play(chess)
        self.assertEqual(turn,"white")
        self.assertEqual(mock_input.call_count,4)
        self.assertEqual(mock_print.call_count,2)


if __name__ == '__main__':
    unittest.main()