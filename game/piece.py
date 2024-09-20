from .cell import Cell 
import sys
sys.stdout.reconfigure(encoding='utf-8')

class Pieces:
    def __init__(self, color, position):
        self.__color__ = color
        # Position debería ser la posicion de la pieza en el tablero!!!
        # ¿Tiene sentido que la pieza sepa en donde esta? Porque eso ya lo sabe el
        # Tablero!
        self.__position__ = position

    def __repr__(self):
        return self.white_repr if self.__color__ == "white" else self.black_repr

    def get_color(self):
        return self.__color__

    def get_position(self):
        return self.__position__

    # # Esto no lo puedo implementar, y si o si lo necesito
    # # 
    # def is_valid(self, old_pos, new_pos):
    #     if self.get_position()
    #     # ¿Que hay en old_pos?
    #     # if old_pos is ocupied:
    #     #   veo que mierda hago
    #     # else:
    #     #   return False   

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

    def valid_moves(self, old_pos, new_pos):
        return (old_pos[0]==new_pos[0] or old_pos[1]==new_pos[1]) and (old_pos!=new_pos)

    def valid_directions(self):
        # Movimientos ortogonales del rook
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))  # (fila, columna)
        return self.possible_moves(board, directions)
    
    def displacement_quantity(self):
        return 8


class Bishop(Pieces):
    white_repr = "♗"
    black_repr = "♝"

    def valid_moves(self, board):
        directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]  # Arriba-Derecha, Arriba-Izquierda, Abajo-Derecha, Abajo-Izquierda
        return self.possible_moves(board, directions)

class Pawn(Pieces):
    white_repr = "♙"
    black_repr = "♟"

    # Color
    # dependiendo del color, estara en la columna 1 o 6
    # entonces para validar el primer moviento destino, me fijo
    # el origen

class Knight(Pieces):
    white_repr = "♘"
    black_repr = "♞"

class King(Pieces):
    white_repr = "♔"
    black_repr = "♚"

class Queen(Pieces):
    white_repr = "♕"
    black_repr = "♛"