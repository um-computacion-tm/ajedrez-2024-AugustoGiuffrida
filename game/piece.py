from .cell import Cell 
import sys
sys.stdout.reconfigure(encoding='utf-8')

class Pieces:
    def __init__(self, color, position):
        self.__color__ = color
        self.__position__ = position

    def __repr__(self):
        return self.white_repr if self.__color__ == "white" else self.black_repr

    def get_color(self):
        return self.__color__

    def get_position(self):
        return self.__position__

    def possible_cell(self, board, moves, new_row, new_col):
        if 0 <= new_row <= 7 and 0 <= new_col <= 7:
            cell = board[new_row][new_col]
            if cell.is_occupied():
                if cell.get_piece().get_color() != self.get_color():
                    moves.append((new_row, new_col))
                return False                    # Detener el bucle de movimientos en esta dirección
            moves.append((new_row, new_col))
            return True                         # Continuar buscando en esta dirección
        return False                            # Fuera del tablero, detener el bucle en esta dirección

    def possible_moves(self, board, directions):
        moves = []
        row, col = self.get_position()

        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = row + i * dr, col + i * dc
                if not self.possible_cell(board, moves, new_row, new_col):
                    break  # Detener la búsqueda en esta dirección si `possible_cell` devuelve False
        return moves


class Rook(Pieces):
    white_repr = "♖"
    black_repr = "♜"

    def __init__(self, color, position):
        super().__init__(color, position)

    def valid_moves(self, board):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (fila, columna)
        return self.possible_moves(board, directions)


class Bishop(Pieces):
    white_repr = "♗"
    black_repr = "♝"

    def valid_moves(self, board):
        directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]  # Arriba-Derecha, Arriba-Izquierda, Abajo-Derecha, Abajo-Izquierda
        return self.possible_moves(board, directions)

class Pawn(Pieces):
    white_repr = "♙"
    black_repr = "♟"

class Knight(Pieces):
    white_repr = "♘"
    black_repr = "♞"

class King(Pieces):
    white_repr = "♔"
    black_repr = "♚"

class Queen(Pieces):
    white_repr = "♕"
    black_repr = "♛"
