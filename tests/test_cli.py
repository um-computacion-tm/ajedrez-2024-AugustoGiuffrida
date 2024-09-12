import unittest
from unittest.mock import patch, MagicMock
from game.cli import Cli
from game.chess import Chess
from game.menu import Menu

class TestCli(unittest.TestCase):

    @patch('your_module.Menu')
    def test_main(self, MockMenu):
        # Configurar el mock para Menu
        mock_menu = MockMenu.return_value
        mock_menu.show_start_menu = MagicMock()
        cli = Cli()
        cli.main()
        # Verificar que Menu fue creado con 'cli'
        MockMenu.assert_called_once_with(cli)
        # Verificar que show_start_menu fue llamado
        mock_menu.show_start_menu.assert_called_once()

    @patch('module.Chess')
    @patch('module.Cli.play')
    def test_start_game(self, MockPlay, MockChess):
        mock_chess = MockChess.return_value
        mock_chess.is_playing.side_effect = [True, True, False]  # Simula dos vueltas del bucle
        cli = Cli()
        cli.start_game()
        # Verificar que Chess fue creado
        MockChess.assert_called_once()
        # Verificar que play se llama mientras is_playing devuelve True
        self.assertEqual(MockPlay.call_count, 2)



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