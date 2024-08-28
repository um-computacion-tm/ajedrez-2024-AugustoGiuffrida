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

    def get_symbol(self):
        return self.__symbol__

class Rook(Pieces):
    white_repr = "♖"
    black_repr = "♜"

class Pawn(Pieces):
    white_repr = "♙"
    black_repr = "♟"
         
class Bishop(Pieces):  
    white_repr = "♗"
    black_repr = "♝"  

class Knight(Pieces):
    white_repr = "♘"
    black_repr = "♞"

class King(Pieces):
    white_repr = "♔"
    black_repr = "♚"


class Queen(Pieces):
    white_repr = "♕"
    black_repr = "♛"


# chess_pieces2 = {
#     "white": {
#         "king": "♔",
#         "queen": "♕",
#         "rook": "♖",
#         "bishop": "♗",
#         "knight": "♘",
#         "pawn": "♙"
#     },
#     "black": {
#         "king": "♚",
#         "queen": "♛",
#         "rook": "♜",
#         "bishop": "♝",
#         "knight": "♞",
#         "pawn": "♟"
#     }
# }