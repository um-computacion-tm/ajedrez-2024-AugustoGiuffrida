from .piece import Pieces, Pawn, Rook, King, Knight, Queen, Bishop
from .exepcions import InvalidPlay
from .board import Board
import json

class Chess:

    def __init__(self):
        self.__turn__= "white"
        self.__board__ = Board()                         # Inicializa el tablero.
        self.__matrix__= self.__board__.get_positions()  # ObtÃ©n las posiciones del tablero.
        self.set_pieces()                                # Coloca las piezas en sus posiciones iniciales.

    @property
    def turn(self):
        return self.__turn__

    @property
    def board(self):
        return self.__board__

    def play(self,source,dest):
        cell = self.__matrix__[source[0]][source[1]]
        if cell.is_occupied():
            turn_color_is_valid = cell.get_piece().get_color() == self.turn
            move_is_valid = self.__board__.is_valid(source,dest)
            if turn_color_is_valid and move_is_valid:
                # Hago la jugada
                return
        raise InvalidPlay

    def is_playing(self):
        return True
   
    def change_turn(self):
        self.__turn__ = "black" if self.__turn__ == "white" else "white"
            
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
        with open('chess_positions.json', 'r') as json_file:
            initial_positions = json.load(json_file)

        for color, pieces in initial_positions.items():
            for piece, positions in pieces.items():
                for position in positions:
                    row, col = position
                    piece_obj = self.make_piece(piece,color, position)
                    self.__matrix__[row][col].place_piece(piece_obj)