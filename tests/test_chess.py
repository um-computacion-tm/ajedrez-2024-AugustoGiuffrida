import unittest
from game.chess import Chess
from game.board import Board  
from game.piece import Pawn, Rook, Knight, Bishop, Queen, King
from unittest.mock import MagicMock, patch
from game.exepcions import InvalidPlay

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    @patch('builtins.print')
    @patch('builtins.exit')
    def test_check_game_over_white_wins(self, mock_exit, mock_print):
        with patch.object(Board, 'king_in_game', side_effect=lambda color: color == "white"):
            self.chess.check_game_over()
            mock_print.assert_called_with("White wins! Black's king has been captured.")
            mock_exit.assert_called_once()

    @patch('builtins.print')
    @patch('builtins.exit')
    def test_check_game_over_black_wins(self, mock_exit, mock_print):
        with patch.object(Board, 'king_in_game', side_effect=lambda color: color == "black"):
            self.chess.check_game_over()
            mock_print.assert_called_with("Black wins! White's king has been captured.")
            mock_exit.assert_called_once()

    @patch('builtins.print')
    @patch('builtins.exit')
    def test_check_game_over_no_winner(self, mock_exit, mock_print):
        with patch.object(Board, 'king_in_game', return_value=True):
            self.chess.check_game_over()
            mock_print.assert_not_called()
            mock_exit.assert_not_called()

    def test_white_piece_captures_black(self):
        source = (1, 1)
        dest = (3, 1)
        white_pawn = Pawn("white")
        self.chess.board.get_cell(source[0], source[1]).place_piece(white_pawn)
        black_pawn = Pawn("black")
        self.chess.board.get_cell(dest[0], dest[1]).place_piece(black_pawn)
        self.chess.move(source, dest)
        self.assertIn(black_pawn, self.chess.white_captures)
        self.assertEqual(self.chess.board.get_cell(dest[0], dest[1]).get_piece(), white_pawn)
        self.assertIsNone(self.chess.board.get_cell(source[0], source[1]).get_piece())

    def test_black_piece_captures_white(self):
        source = (6, 1)
        dest = (5, 1)
        black_pawn = Pawn("black")
        self.chess.board.get_cell(source[0], source[1]).place_piece(black_pawn)
        white_pawn = Pawn("white")
        self.chess.board.get_cell(dest[0], dest[1]).place_piece(white_pawn)
        self.chess.move(source, dest)
        self.assertIn(white_pawn, self.chess.black_captures)
        self.assertEqual(self.chess.board.get_cell(dest[0], dest[1]).get_piece(), black_pawn)
        self.assertIsNone(self.chess.board.get_cell(source[0], source[1]).get_piece())


    def test_move_no_capture(self):
        source = (1, 1)
        dest = (3, 1)
        white_pawn = Pawn("white")
        self.chess.board.get_cell(source[0], source[1]).place_piece(white_pawn)
        self.chess.move(source, dest)
        self.assertEqual(self.chess.board.get_cell(dest[0], dest[1]).get_piece(), white_pawn)
        self.assertIsNone(self.chess.board.get_cell(source[0], source[1]).get_piece())
        self.assertEqual(len(self.chess.white_captures), 0)
        self.assertEqual(len(self.chess.black_captures), 0)

    def test_play_valid_move(self):
        source = (1, 1)
        dest = (2, 1)
        white_pawn = Pawn("white")
        self.chess.board.get_cell(source[0], source[1]).place_piece(white_pawn)
        with patch.object(Board, 'is_valid', return_value=True):
            self.chess.play(source, dest)
            self.assertEqual(self.chess.turn, "black")

    def test_play_invalid_move(self):
        source = (1, 1)
        dest = (2, 1)
        white_pawn = Pawn("white")
        self.chess.board.get_cell(source[0], source[1]).place_piece(white_pawn)
        with patch.object(Board, 'is_valid', return_value=False):
            with self.assertRaises(InvalidPlay):
                self.chess.play(source, dest)

    def test_initial_turn(self):
        self.assertEqual(self.chess.turn, "white")

    def test_play(self):
        chess = Chess()
        board = chess.board.get_positions()
        source = (0, 0)
        dest = (1, 1)
        cell = board[source[0]][source[1]]
        piece_mock = MagicMock()
        piece_mock.get_color.return_value = "white"
        piece_mock.valid_moves.return_value = True
        cell.is_occupied = MagicMock(return_value=True)
        cell.get_piece = MagicMock(return_value=piece_mock)
        chess.board.is_valid = MagicMock(return_value=True)
        chess.move = MagicMock()
        chess.change_turn = MagicMock()
        chess.play(source, dest)
        chess.board.is_valid.assert_called_once_with(source, dest)
        chess.move.assert_called_once_with(source, dest)
        chess.change_turn.assert_called_once()

    def test_play_invalid(self):
        chess = Chess()
        board = chess.board.get_positions()
        source = (0, 0)
        dest = (1, 1)
        cell = board[source[0]][source[1]]
        piece_mock = MagicMock()
        piece_mock.get_color.return_value = "white"
        piece_mock.valid_moves.return_value = False
        cell.is_occupied = MagicMock(return_value=True)
        cell.get_piece = MagicMock(return_value=piece_mock)
        with self.assertRaises(InvalidPlay):
            chess.play(source, dest)

    def test_change_turn(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "black")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "white")

    def test_board_initialization(self):
        board = self.chess.board.get_positions()
        self.assertEqual(len(board), 8)
        self.assertEqual(len(board[0]), 8)

    def test_make_piece(self):
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
        self.assertEqual(piece,'♚')
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
