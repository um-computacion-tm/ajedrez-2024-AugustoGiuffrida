from .cell import Cell 
import sys
sys.stdout.reconfigure(encoding='utf-8')

class Pieces:
    def __init__(self, color):
        self.__color__ = color

    def __repr__(self):
        return self.white_repr if self.__color__ == "white" else self.black_repr

    def get_color(self):
        return self.__color__


class Rook(Pieces):
    white_repr = "♖"
    black_repr = "♜"

    def valid_moves(self, old_pos, new_pos):
        return (old_pos[0]==new_pos[0] or old_pos[1]==new_pos[1]) and (old_pos!=new_pos)

    
class Bishop(Pieces):
    white_repr = "♗"
    black_repr = "♝"

    def valid_moves(self, old_pos, new_pos):
        return abs(new_pos[0] - old_pos[0]) == abs(new_pos[1] - old_pos[1]) and (old_pos != new_pos)


class Knight(Pieces):
    white_repr = "♘"
    black_repr = "♞"

    def valid_moves(self, old_pos, new_pos):
        return (abs(new_pos[1] - old_pos[1]) == 1 and abs(new_pos[0] - old_pos[0]) == 2) or \
               ((abs(new_pos[1] - old_pos[1]) == 2 and abs(new_pos[0] - old_pos[0]) == 1) and old_pos != new_pos)


class Pawn(Pieces):
    white_repr = "♙"
    black_repr = "♟"

class Pawn(Pieces):
    white_repr = "♙"
    black_repr = "♟"
    
    def valid_moves(self, source, dest):
        if self.get_color() == "white":
            return self._valid_white_moves(source, dest)
        elif self.get_color() == "black":
            return self._valid_black_moves(source, dest)
        return False
    
    def _valid_white_moves(self, source, dest):
        if self._move_forward(source, dest, direction=1):  # Movimiento hacia adelante
            return True
        if self._initial_double_move(source, dest, direction=1):  # Primer movimiento: puede avanzar dos casillas
            return True
        if self._capture_diagonal(source, dest, direction=1):  # Captura diagonal
            return True
        return False
    
    def _valid_black_moves(self, source, dest):
        if self._move_forward(source, dest, direction=-1):  # Movimiento hacia adelante
            return True
        if self._initial_double_move(source, dest, direction=-1):  # Primer movimiento: puede avanzar dos casillas
            return True
        if self._capture_diagonal(source, dest, direction=-1):  # Captura diagonal
            return True
        return False

    def _move_forward(self, source, dest, direction):
        # Mover una casilla hacia adelante
        return (dest[0] - source[0] == direction) and (source[1] == dest[1])

    def _initial_double_move(self, source, dest, direction):
        # Primer movimiento: puede avanzar dos casillas
        start_row = 1 if direction == 1 else 6
        return (source[0] == start_row) and (dest[0] == source[0] + (2 * direction)) and (source[1] == dest[1])

    def _capture_diagonal(self, source, dest, direction):
        # Captura diagonal
        return (dest[0] - source[0] == direction) and (abs(source[1] - dest[1]) == 1)





class King(Pieces):
    white_repr = "♔"
    black_repr = "♚"

    def valid_moves(self, old_pos, new_pos):
        return abs(old_pos[0]-new_pos[0])<=1 and abs(old_pos[1]-new_pos[1]) <=1 and (old_pos != new_pos)

class Queen(Pieces):
    white_repr = "♕"
    black_repr = "♛"

    def valid_moves(self, old_pos, new_pos):
        # Verificar que las posiciones no sean iguales
        if old_pos == new_pos:
            return False
        
        # Movimiento horizontal o vertical
        return (old_pos[0] == new_pos[0] or old_pos[1] == new_pos[1]) or \
              (abs(new_pos[0] - old_pos[0]) == abs(new_pos[1] - old_pos[1]))




    