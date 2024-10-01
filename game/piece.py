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

    def valid_moves(self, old_pos, new_pos, is_capture=False):
        direction = 1 if self.get_color() == "white" else -1

        # Movimiento hacia adelante
        if not is_capture:
            # Si es el primer movimiento, puede moverse 2 casillas hacia adelante
            if old_pos[0] == (1 if self.get_color() == "white" else 6):
                return new_pos[0] == old_pos[0] + 2 * direction and old_pos[1] == new_pos[1] or \
                       new_pos[0] == old_pos[0] + 1 * direction and old_pos[1] == new_pos[1]
            # Movimiento normal (una casilla hacia adelante)
            else:
                return new_pos[0] == old_pos[0] + direction and old_pos[1] == new_pos[1]

        # Captura diagonal
        else:
            return new_pos[0] == old_pos[0] + direction and abs(new_pos[1] - old_pos[1]) == 1



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




    