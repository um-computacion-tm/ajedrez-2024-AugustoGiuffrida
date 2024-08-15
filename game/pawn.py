from .piece import Pieces

class Pawn(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        if color == "white":
            self.__symbol__ = "♙"
        else:
            self.__symbol__ = "♟"

    def valid_moves(self, board):
        pass