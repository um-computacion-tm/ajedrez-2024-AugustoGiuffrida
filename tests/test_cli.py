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
    @patch('game.cli.Cli.range_input', side_effect=[(0, 0), (1, 0)])  # Simula entradas de usuario para old_pos y new_pos
    @patch('game.chess.Chess.play')  # Mock del método play de Chess
    def test_start_game_turn(self, mock_play, mock_range_input, mock_print, mock_board, mock_is_playing):
        mock_board.show_board.return_value = "Board"  # Simula el retorno de show_board
        cli = Cli()
        cli.start_game()

        # Verificar que se llama a Chess.is_playing dos veces
        self.assertEqual(mock_is_playing.call_count, 2)

        # Verificar que se muestra el tablero y el turno
        mock_print.assert_any_call("Turn: ", mock.ANY)
        mock_print.assert_any_call("Board")

        # Verificar que Chess.play es llamado con las posiciones correctas
        mock_play.assert_called_once_with((0, 0), (1, 0))


    @patch('builtins.input', side_effect=['z9', 'a2'])  # Simula entradas inválidas y válidas
    @patch('builtins.print')  # Mock de print para verificar los mensajes
    def test_range_input_invalid(self, mock_print, mock_input):
        cli = Cli()
        result = cli.range_input("Enter initial position: ")

        # Verifica que la entrada final válida es (1, 0)
        self.assertEqual(result, (1, 0))

        # Verifica que se impriman los mensajes de error correspondientes
        mock_print.assert_any_call("\nInvalid column or row value.\n")
        mock_print.assert_any_call("Invalid Input. Please try again.")


if __name__ == '__main__':
    unittest.main()
