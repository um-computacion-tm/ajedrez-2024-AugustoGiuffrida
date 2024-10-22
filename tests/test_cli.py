import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from game.cli import Cli
from game.chess import Chess
from game.exepcions import InvalidPlay

class TestCli(unittest.TestCase):

    @patch.object(Chess, 'is_playing', side_effect=[False])
    def test_start_game_immediately_stops(self, mock_is_playing):
        cli = Cli()
        cli.start_game()
        mock_is_playing.assert_called_once()

    @patch('game.chess.Chess.is_playing', side_effect=[True, False])
    @patch('game.chess.Chess.board', new_callable=MagicMock)
    @patch('builtins.print')
    @patch('game.cli.Cli.validate_input', side_effect=[(0, 0), (1, 0)])
    @patch('game.chess.Chess.play')  
    def test_start_game_turn(self, mock_play, mock_validate_input, mock_print, mock_board, mock_is_playing):
        mock_board.show_board.return_value = "Board"
        cli = Cli()
        cli.start_game()

        # Verificar que se llama a Chess.is_playing dos veces
        self.assertEqual(mock_is_playing.call_count, 2)

        # Verificar que se muestra el tablero y el turno
        mock_print.assert_any_call("Turn: ", mock.ANY)
        mock_print.assert_any_call("Board")

        # Verificar que Chess.play es llamado con las posiciones correctas
        mock_play.assert_called_once_with((0, 0), (1, 0))

    @patch('game.chess.Chess.is_playing', side_effect=[True, True, False])
    @patch('game.chess.Chess.board', new_callable=MagicMock)
    @patch('builtins.print')
    @patch('game.cli.Cli.validate_input', side_effect=[(0, 0), (1, 0), (0, 0), (1, 0)])
    @patch.object(Chess, 'play', side_effect=InvalidPlay())  
    def test_invalid_play(self, mock_play, mock_validate_input, mock_print, mock_board, mock_is_playing):
        mock_board.show_board.return_value = "Board"
        cli = Cli()
        cli.start_game()

        # Verificar que se llama a Chess.is_playing dos veces
        self.assertEqual(mock_is_playing.call_count, 3)

        # Verificar que se muestra el tablero y el turno
        mock_print.assert_any_call("Turn: ", mock.ANY)
        mock_print.assert_any_call("Board")

        # Verificar que Chess.play es llamado con las posiciones correctas
        mock_play.assert_any_call((0, 0), (1, 0)
        )
        self.assertEqual(mock_play.call_count, 2)


    @patch('builtins.input', side_effect=['z9', 'a2'])  # Entrada inválida y válida
    @patch('builtins.print')  
    def test_validate_input_invalid(self, mock_print, mock_input):
        cli = Cli()
        result = cli.validate_input("Enter initial position: ")

        # Verifica que la entrada final válida es (1, 0)
        self.assertEqual(result, (2, 0))

        # Verifica que se impriman los mensajes de error correspondientes
        mock_print.assert_any_call("\nInvalid column or row value.\n")


    @patch('builtins.print')
    def test_convert_position_invalid_length(self, mock_print):
        cli = Cli()
        result = cli.convert_position('a12')  # Entrada con longitud inválida
        self.assertFalse(result)

        # Verifica que se imprime el mensaje de longitud inválida
        mock_print.assert_any_call("\nInvalid input length.\n")

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1a'])  # Provocará un ValueError
    def test_convert_position_value_error(self, mock_input, mock_print):
        cli = Cli()
        result = cli.convert_position('1a')  # Simulamos entrada que causará un ValueError
        self.assertFalse(result)



if __name__ == '__main__':
    unittest.main()
