import unittest
from game.chess import Chess
from game.piece import Pawn, Rook, Knight, Bishop, Queen, King
from unittest.mock import MagicMock
from game.exepcions import InvalidPlay

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_initial_turn(self):
        # Verifica que el turno inicial es "white"
        self.assertEqual(self.chess.turn, "white")

    def test_play(self):
        chess = Chess()
        board = chess.board.get_positions()
        source = (0, 0)
        dest = (1, 1)

        # Acceder a la celda
        cell = board[source[0]][source[1]]

        # Crear mock de la pieza
        piece_mock = MagicMock()
        piece_mock.get_color.return_value = "white"
        piece_mock.valid_moves.return_value = True

        # Mockear la celda para que devuelva la pieza y esté ocupada
        cell.is_occupied = MagicMock(return_value=True)
        cell.get_piece = MagicMock(return_value=piece_mock)

        # Mockear el método is_valid del board
        chess.board.is_valid = MagicMock(return_value=True)

        # Mockear los métodos move y change_turn
        chess.move = MagicMock()
        chess.change_turn = MagicMock()  # Corregir esta línea para que sea un mock

        # Ejecutar la función play
        chess.play(source, dest)

        # Verificar que el método is_valid fue llamado correctamente
        chess.board.is_valid.assert_called_once_with(source, dest)

        # Verificar que se llamó a move con las posiciones correctas
        chess.move.assert_called_once_with(source, dest)

        # Verificar que se llamó a change_turn
        chess.change_turn.assert_called_once()

    def test_play_invalid(self):
        chess = Chess()
        board = chess.board.get_positions()
        source = (0, 0)
        dest = (1, 1)

        cell = board[source[0]][source[1]]

        piece_mock = MagicMock()
        piece_mock.get_color.return_value = "white"
        piece_mock.valid_moves.return_value = False  # Movimiento no válido

        cell.is_occupied = MagicMock(return_value=True)
        cell.get_piece = MagicMock(return_value=piece_mock)

        # No es necesario mockear is_valid en este caso
        # chess.board.is_valid = MagicMock(return_value=True)  # Esto ya no es necesario

        # Verificar que se lanza InvalidPlay
        with self.assertRaises(InvalidPlay):
            chess.play(source, dest)


    def test_change_turn(self):
        # Cambia de turno y verifica que ahora es "black"
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "black")

        # Cambia de turno nuevamente y verifica que es "white"
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "white")

    def test_board_initialization(self):
        # Verifica que el tablero fue inicializado correctamente
        board = self.chess.board.get_positions()
        self.assertEqual(len(board), 8)
        self.assertEqual(len(board[0]), 8)

    def test_make_piece(self):
        # Verifica la creación de una pieza
        piece = self.chess.make_piece("pawn", "white")
        self.assertIsInstance(piece, Pawn)

        piece = self.chess.make_piece("rook", "black")
        self.assertIsInstance(piece, Rook)

        piece = self.chess.make_piece("knight", "white")
        self.assertIsInstance(piece, Knight)

        piece = self.chess.make_piece("bishop", "black")
        self.assertIsInstance(piece, Bishop)

        piece = self.chess.make_piece("queen", "white")
        self.assertIsInstance(piece, Queen)

        piece = self.chess.make_piece("king", "black")
        self.assertIsInstance(piece, King)

    def test_set_pieces_white(self):
        chess = Chess()
        board = chess.board.get_positions()

        piece = str(board[0][0].get_piece())
        self.assertEqual(piece,'♖')
        
        piece = str(board[0][1].get_piece())
        self.assertEqual(piece,'♘')
        
        piece = str(board[0][2].get_piece())
        self.assertEqual(piece,'♗')
        
        piece = str(board[0][3].get_piece())
        self.assertEqual(piece,'♕')
        
        piece = str(board[0][4].get_piece())
        self.assertEqual(piece,'♔')
        
        piece = str(board[0][5].get_piece())
        self.assertEqual(piece,'♗')
        
        piece = str(board[0][6].get_piece())
        self.assertEqual(piece,'♘')
        
        piece = str(board[0][7].get_piece())
        self.assertEqual(piece,'♖')

        # Verificar los peones negros en la fila 1
        for col in range(8):
            piece = str(board[1][col].get_piece())
            self.assertEqual(piece,'♙')

    def test_set_pieces_black(self):
        chess = Chess()
        board = chess.board.get_positions()
        
        piece = str(board[7][0].get_piece())
        self.assertEqual(piece, '♜')
        
        piece = str(board[7][1].get_piece())
        self.assertEqual(piece, '♞')
        
        piece = str(board[7][2].get_piece())
        self.assertEqual(piece, '♝')
        
        piece = str(board[7][3].get_piece())
        self.assertEqual(piece, '♛')
        
        piece = str(board[7][4].get_piece())
        self.assertEqual(piece,'♚' )
        
        piece = str(board[7][5].get_piece())
        self.assertEqual(piece,'♝')
        
        piece = str(board[7][6].get_piece())
        self.assertEqual(piece, '♞')
        
        piece = str(board[7][7].get_piece())
        self.assertEqual(piece, '♜')

        for col in range(8):
            piece = str(board[6][col].get_piece())
            self.assertEqual(piece, '♟')



if __name__ == "__main__":
    unittest.main()