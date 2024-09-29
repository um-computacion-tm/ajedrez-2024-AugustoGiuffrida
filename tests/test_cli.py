import unittest
from unittest.mock import patch, MagicMock, call
from game.cli import Cli
from game.chess import Chess
#from game.menu import Menu

class TestCli(unittest.TestCase):

    @patch('game.chess.Chess.is_playing', side_effect=[False])
    def test_start_game_immediately_stops(self, mock_is_playing):
        cli = Cli()
        cli.start_game()
        mock_is_playing.assert_called_once()

    # @patch('game.chess.Chess.is_playing')
    # @patch('game.cli.Cli.range_input')
    # @patch('game.board.Board.show_board')
    # @patch('game.chess.Chess.turn')
    # @patch('builtins.print')
    # @patch('game.chess.Chess.play')
    # def test_start_game_valid_positions(self, mock_is_playing, mock_range_input, mock_show_board, mock_chess_turn, mock_print,  mock_play):
    #     cli = Cli()
    #     print('one')
    #     cli.start_game()
    #     mock_is_playing.side_effect = True
    #     self.assertIsInstance(cli.start_game.chess, Chess)
    #     mock_show_board.side_effect = 'Tablero xd'
    #     mock_chess_turn.side_effect = 'white'
    #     mock_print.assert_has_calls([call("Tablero xd"), call("Turn: white")])
    #     mock_range_input.side_effect = [0, 0]
    #     mock_range_input.side_effect = [1, 1]
    #     self.assertEqual(mock_print.call_count, 2)
    #     mock_is_playing.side_effect = False

    # @patch('game.chess.Chess')  # Mockea el objeto Chess.
    # @patch('game.cli.Cli.range_input')  # Simula entradas de coordenadas.
    # @patch('builtins.print')  # Mockea el print para evitar que imprima en los tests.
    # def test_start_game(self, mock_chess, mock_range_input, mock_print):
    #     # Instancia el mock del objeto Chess.

    #     cli = Cli()
    #     cli.start_game()

    #     mock_chess_instance = mock_chess.return_value
    #     mock_chess_instance.is_playing.side_effect = [True, False]  # Simula que el juego empieza y luego termina.
        
    #     mock_chess_instance.play = MagicMock()
        
    #     # Verificar que se llamó a chess.play una vez con las coordenadas correctas.
    #     mock_range_input.side_effect = [0, 0]
    #     mock_range_input.side_effect = [1, 1]

    #     mock_chess_instance.play.assert_called_once_with((0, 0), (1, 1))
    #     # Verificar que el ciclo terminó cuando is_playing() devolvió False.
    #     self.assertEqual(mock_chess_instance.is_playing.call_count, 2)

    #     # Verificar que los prints relevantes se llamaron, sin mostrar el tablero.
    #     mock_print.assert_any_call("Turn: ", mock_chess_instance.turn)

    # @patch('builtins.input', side_effect=['a', '1', '1', '2', '2'])
    # @patch('builtins.print')
    # @patch('os.get_terminal_size', return_value=MagicMock(columns=80))  # Simular tamaño de terminal
    # def test_play_sad(self, mock_get_terminal_size, mock_print, mock_input):
    #     chess = Chess()
    #     cli = Cli()
    #     cli.start_game()
    #     self.assertEqual(mock_input.call_count, 5)
    #     self.assertEqual(mock_print.call_count, 3)
    #     mock_print.assert_any_call("Entrada no válida. Por favor, introduce un número entre 0 y 7.")
    #     self.assertEqual(chess.turn, "black")

if __name__ == '__main__':
    unittest.main()
