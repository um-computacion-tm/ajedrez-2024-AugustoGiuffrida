from .piece import Pieces, Pawn, Rook, King, Knight, Queen, Bishop
from .exepcions import InvalidPlay
from .board import Board
from .cell import Cell
import json
import os

class Chess:

    def __init__(self):
        self.__turn__= "white"
        self.__board__ = Board()                         # Inicializa el tablero.
        self.__matrix__= self.__board__.get_positions()  # ObtÃ©n las posiciones del tablero.
        self.set_pieces()                                # Coloca las piezas en sus posiciones iniciales.                            
        self.white_captures = []                         # Piezas capturadas por las blancas
        self.black_captures = []                         # Piezas capturadas por las negras

    @property
    def turn(self):
        return self.__turn__

    @property
    def board(self):
        return self.__board__

    def is_playing(self):
        return True

    def play(self, source, dest):
        cell = self.__matrix__[source[0]][source[1]]

        if cell.is_occupied():
            piece = cell.get_piece()
            turn_color_is_valid = piece.get_color() == self.turn
            move_is_valid = self.__board__.is_valid(source, dest)

            if turn_color_is_valid and move_is_valid:
                self.move(source, dest)
                self.check_game_over()
                self.change_turn()
                os.system('cls' if os.name == 'nt' else 'clear')
                return

        raise InvalidPlay(f"Invalid move from {source} to {dest}.")

    def check_game_over(self):
        white_king_alive = self.__board__.king_in_game("white")
        black_king_alive = self.__board__.king_in_game("black")

        if not white_king_alive:
            print("Black wins! White's king has been captured.")
            exit()
        elif not black_king_alive:
            print("White wins! Black's king has been captured.")
            exit()


    def move(self, source, dest):
        old_cell = self.__board__.get_cell(source[0], source[1])
        new_cell = self.__board__.get_cell(dest[0], dest[1])

        if new_cell.is_occupied():
            captured_piece = new_cell.get_piece()
            if captured_piece.get_color() == "white":
                self.black_captures.append(captured_piece)  # Las negras capturan
            else:
                self.white_captures.append(captured_piece)  # Las blancas capturan

        new_cell.place_piece(old_cell.remove_piece())

   
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