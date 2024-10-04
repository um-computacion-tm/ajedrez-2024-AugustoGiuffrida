from .piece import Pieces, Pawn, Rook, King, Knight, Queen, Bishop
from .exepcions import InvalidPlay
from .board import Board
from .cell import Cell
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

    def play(self, source, dest):
        cell = self.__matrix__[source[0]][source[1]]

        # Depuración para verificar la celda
        #print(f"Source Cell: {source}, Occupied: {cell.is_occupied()}")
        
        if cell.is_occupied():
            piece = cell.get_piece()
            #print(f"Piece at Source: {piece}, Color: {piece.get_color() if piece else 'None'}")
            
            turn_color_is_valid = piece.get_color() == self.turn
            move_is_valid = self.__board__.is_valid(source, dest)

            # Depuración para verificar condiciones
            #print(f"Turn color valid: {turn_color_is_valid}, Move valid: {move_is_valid}")

            if turn_color_is_valid and move_is_valid:
                self.move(source, dest)
                self.change_turn()
                return

        raise InvalidPlay


    def move(self, source, dest):
        old_cell = self.__board__.get_cell(source[0], source[1])  # Cambiado
        new_cell = self.__board__.get_cell(dest[0], dest[1])      # Cambiado
        new_cell.place_piece(old_cell.remove_piece())


    def is_playing(self):
        return True
   
    def change_turn(self):
        self.__turn__ = "black" if self.__turn__ == "white" else "white"

            
    def make_piece(self, piece, color):
        piece_classes = {
            "pawn": Pawn,
            "rook": Rook,
            "knight": Knight,
            "bishop": Bishop,
            "queen": Queen,
            "king": King
        }
        return piece_classes[piece](color) if piece in piece_classes else None
        
    def set_pieces(self):
        with open('chess_positions.json', 'r') as json_file:
            initial_positions = json.load(json_file)

        for color, pieces in initial_positions.items():
            for piece, positions in pieces.items():
                for position in positions:
                    row, col = position
                    piece_obj = self.make_piece(piece,color)
                    self.__matrix__[row][col].place_piece(piece_obj)