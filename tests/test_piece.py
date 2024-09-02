import unittest
from game.piece import Pieces, Rook, Pawn
from game.cell import Cell

class TestPieces(unittest.TestCase):

    def setUp(self):
        self.board = [[Cell("white", (i, j)) for j in range(8)] for i in range(8)]
        self.rook = Rook("white", (4, 4))
        self.pawn = Pawn("white", (6, 0))

    def test_piece_initialization(self):
        piece = Pieces("white", (0, 0))
        self.assertEqual(piece.get_color(), "white")
        self.assertEqual(piece.get_position(), (0, 0))
    
    def place_piece(self, piece, row, col):
        # Método auxiliar para colocar piezas en el tablero
        self.board[row][col].place_piece(piece)
    
    def test_rook_moves_empty_board(self):
        # Test: Rook en el centro del tablero con movimientos libres
        rook = Rook("white", (4, 4))
        self.place_piece(rook, 4, 4)

        expected_moves = [
            (3, 4), (2, 4), (1, 4), (0, 4),  # Movimientos hacia arriba
            (5, 4), (6, 4), (7, 4),          # Movimientos hacia abajo
            (4, 3), (4, 2), (4, 1), (4, 0),  # Movimientos hacia la izquierda
            (4, 5), (4, 6), (4, 7)           # Movimientos hacia la derecha
        ]

        moves = rook.valid_moves(self.board)
        self.assertCountEqual(moves, expected_moves)

    def test_rook_moves_blocked_by_same_color(self):
        # Test: Rook bloqueada por piezas del mismo color
        rook = Rook("white", (4, 4))
        self.place_piece(rook, 4, 4)
        self.place_piece(Rook("white", (2, 4)), 2, 4)  # Bloqueo arriba
        self.place_piece(Rook("white", (4, 6)), 4, 6)  # Bloqueo derecha

        expected_moves = [
            (3, 4),                         # Movimientos hacia arriba hasta la pieza del mismo color
            (5, 4), (6, 4), (7, 4),         # Movimientos hacia abajo
            (4, 3), (4, 2), (4, 1), (4, 0), # Movimientos hacia la izquierda
            (4, 5)                          # Movimientos hacia la derecha hasta la pieza del mismo color
        ]

        moves = rook.valid_moves(self.board)
        self.assertCountEqual(moves, expected_moves)

    def test_rook_moves_capture_opposite_color(self):
        # Test: Rook captura piezas del color contrario
        rook = Rook("white", (4, 4))
        self.place_piece(rook, 4, 4)
        self.place_piece(Rook("black", (2, 4)), 2, 4)  # Captura arriba
        self.place_piece(Rook("black", (4, 6)), 4, 6)  # Captura derecha

        expected_moves = [
            (3, 4), (2, 4),                     # Movimientos hacia arriba con captura
            (5, 4), (6, 4), (7, 4),             # Movimientos hacia abajo
            (4, 3), (4, 2), (4, 1), (4, 0),     # Movimientos hacia la izquierda
            (4, 5), (4, 6)                      # Movimientos hacia la derecha con captura
        ]

        moves = rook.valid_moves(self.board)
        self.assertCountEqual(moves, expected_moves)

if __name__ == '__main__':
    unittest.main()
