import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from game.cli import Cli
from game.chess import Chess
from game.exepcions import InvalidPlay

class TestCli(unittest.TestCase):

    @patch('game.chess.Chess.is_playing', side_effect=[False])
    def test_start_game_immediately_stops(self, mock_is_playing):
        cli = Cli()
        cli.start_game()
        mock_is_playing.assert_called_once()

    @patch('game.chess.Chess.is_playing', side_effect=[True, False])
    @patch('game.chess.Chess.board', new_callable=MagicMock)  # Parchear el atributo board
    @patch('builtins.print')  # Para evitar que imprima en la consola durante el test
    @patch('game.cli.Cli.range_input', side_effect=[0, 0, 1, 0])  # Simula entradas de usuario para old_pos y new_pos
    @patch('game.chess.Chess.play')  # Mock del método play de Chess
    def test_start_game_turn(self, mock_play, mock_range_input, mock_print, mock_board, mock_is_playing):
        mock_board.show_board.return_value = "Board"  # Simula el retorno de show_board
        cli = Cli()
        cli.start_game()

        # Verificar que se llama a Chess.is_playing dos veces
        self.assertEqual(mock_is_playing.call_count, 2)

        # Verificar que se muestra el tablero y el turno
        mock_print.assert_any_call("Turn: ", mock.ANY)  # Cambiar 'mock' a 'mock'
        mock_print.assert_any_call("Board")

        # Verificar que Chess.play es llamado con las posiciones correctas
        mock_play.assert_called_once_with((0, 0), (1, 0))


    @patch('builtins.input', side_effect=['8', '-1', 'a', '2'])  # Simula entradas fuera de rango o inválidas
    @patch('builtins.print')  # Mock de print para verificar los mensajes
    def test_range_input_invalid(self, mock_print, mock_input):
        cli = Cli()
        result = cli.range_input("From row (0-7): ")
        self.assertEqual(result, 2)  # Asegurarse de que la entrada válida se retorna al final

        # Verifica que se imprime el mensaje de error correcto
        mock_print.assert_any_call("Las coordenadas están fuera del rango permitido (0-7). Inténtalo de nuevo")
        mock_print.assert_any_call("Entrada no válida. Por favor, introduce un número entre 0 y 7.")

if __name__ == '__main__':
    unittest.main()
