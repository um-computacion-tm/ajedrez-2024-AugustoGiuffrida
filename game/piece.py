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

    def valid_moves(self, source, dest):
        # Movimiento hacia adelante
        if self.get_color() == "white":
            # Mover una casilla hacia adelante
            if source[0] - dest[0] == 1 and source[1] == dest[1]:
                return True
            # Primer movimiento: puede avanzar dos casillas
            if source[0] == 6 and dest[0] == 4 and source[1] == dest[1]:
                return True
            # Captura diagonal
            if source[0] - dest[0] == 1 and abs(source[1] - dest[1]) == 1:
                return True
        elif self.get_color() == "black":
            # Mover una casilla hacia adelante
            if dest[0] - source[0] == 1 and source[1] == dest[1]:
                return True
            # Primer movimiento: puede avanzar dos casillas
            if source[0] == 1 and dest[0] == 3 and source[1] == dest[1]:
                return True
            # Captura diagonal
            if dest[0] - source[0] == 1 and abs(source[1] - dest[1]) == 1:
                return True
        return False




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




    