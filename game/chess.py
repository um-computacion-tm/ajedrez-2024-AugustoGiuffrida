from .board import Board
from .piece import Pieces, Pawn, Rook, King, Knight, Queen, Bishop

class Chess:

    def __init__(self):
        self.__turn__= "white"
        self.__board__ = Board()                         # Inicializa el tablero.
        self.__matrix__= self.__board__.get_positions()  # Obtén las posiciones del tablero.
        self.set_pieces()                                # Coloca las piezas en sus posiciones iniciales.

    @property
    def turn(self):
        return self.__turn__

    def board(self):
        return self.__board__

    def is_playing(self):
        return True
   
   
    def change_turn(self):
        if self.__turn__ == "white":
            self.__turn__ = "black"
        else:
            self.__turn__ = "white"

    def make_piece(self, piece, color, position):
        piece_classes = {
            "pawn": Pawn,
            "rook": Rook,
            "knight": Knight,
            "bishop": Bishop,
            "queen": Queen,
            "king": King
        }
        return piece_classes[piece](color, position) if piece in piece_classes else None
        
    def set_pieces(self):
        initial_positions = {
            "white": {
                "rook": [(7, 0), (7, 7)],  
                "knight": [(7, 1), (7, 6)],  
                "bishop": [(7, 2), (7, 5)],  
                "queen": [(7, 3)],  
                "king": [(7, 4)], 
                "pawn": [(6, i) for i in range(8)]  
            },
            "black": {
                "rook": [(0, 0), (0, 7)],  
                "knight": [(0, 1), (0, 6)], 
                "bishop": [(0, 2), (0, 5)],  
                "queen": [(0, 3)],  
                "king": [(0, 4)],  
                "pawn": [(1, i) for i in range(8)]  
            }
        }

        for color, pieces in initial_positions.items():
            for piece, positions in pieces.items():
                for position in positions:
                    row, col = position
                    piece_obj = self.make_piece(piece,color, position)
                    self.__matrix__[row][col].place_piece(piece_obj)



