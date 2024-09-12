from .cell import Cell 
import sys
sys.stdout.reconfigure(encoding='utf-8')

class Pieces:
    def __init__(self, color, position, white_repr, black_repr, directions=None):
        self.__color__ = color
        self.__position__ = position
        self.white_repr = white_repr
        self.black_repr = black_repr
        self.directions = directions if directions else []

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
                return False  # Detener el bucle de movimientos en esta dirección
            moves.append((new_row, new_col))
            return True  # Continuar buscando en esta dirección
        return False  # Fuera del tablero, detener el bucle en esta dirección

    def possible_moves(self, board):
        moves = []
        row, col = self.get_position()

        for dr, dc in self.directions:
            for i in range(1, 8):
                new_row, new_col = row + i * dr, col + i * dc
                if not self.possible_cell(board, moves, new_row, new_col):
                    break  # Detener la búsqueda en esta dirección si `possible_cell` devuelve False
        return moves

# Clases específicas para cada pieza, pasando las direcciones al constructor
class Rook(Pieces):
    def __init__(self, color, position):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (fila, columna)
        super().__init__(color, position, "♖", "♜", directions)

class Bishop(Pieces):
    def __init__(self, color, position):
        directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]  # Arriba-Derecha, Arriba-Izquierda, Abajo-Derecha, Abajo-Izquierda
        super().__init__(color, position, "♗", "♝", directions)

class Queen(Pieces):
    def __init__(self, color, position):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]  # Todas las direcciones posibles
        super().__init__(color, position, "♕", "♛", directions)

class Pawn(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position, "♙", "♟")

class Knight(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position, "♘", "♞")

class King(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position, "♔", "♚")
