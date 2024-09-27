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


    # # Esto no lo puedo implementar, y si o si lo necesito
    # # 
    # def is_valid(self, old_pos, new_pos):
    #     if self.get_position()
    #     # ¿Que hay en old_pos?
    #     # if old_pos is ocupied:
    #     #   veo que mierda hago
    #     # else:
    #     #   return False   


class Rook(Pieces):
    white_repr = "♖"
    black_repr = "♜"

    def __init__(self, color, ):
        super().__init__(color)

    def valid_moves(self, old_pos, new_pos):
        return (old_pos[0]==new_pos[0] or old_pos[1]==new_pos[1]) and (old_pos!=new_pos)

    
class Bishop(Pieces):
    white_repr = "♗"
    black_repr = "♝"

    def valid_moves(self, old_pos, new_pos):
        return abs(new_pos[0] - old_pos[0]) == abs(new_pos[1] - old_pos[1]) and old_pos != new_pos


class Knight(Pieces):
    white_repr = "♘"
    black_repr = "♞"

    def valid_moves(self, old_pos, new_pos):
        return (abs(new_pos[1] - old_pos[1]) == 1 and abs(new_pos[0] - old_pos[0]) == 2) or \
               (abs(new_pos[1] - old_pos[1]) == 2 and abs(new_pos[0] - old_pos[0]) == 1)


class Pawn(Pieces):
    white_repr = "♙"
    black_repr = "♟"

    # Color
    # dependiendo del color, estara en la columna 1 o 6
    # entonces para validar el primer moviento destino, me fijo
    # el origen


class King(Pieces):
    white_repr = "♔"
    black_repr = "♚"

class Queen(Pieces):
    white_repr = "♕"
    black_repr = "♛"



    