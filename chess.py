from game.board import Board
from game.piece import Pieces, Pawn, Rook, King, Knight, Queen, Bishop

class Chess:

    def __init__(self):
        #self.__board__ = Board()
        #self.__matrix__ = __make_board__.get_position()

        self.__board__ = Board()  # Inicializa el tablero.
        self.__matrix__= self.__board__.get_positions()  # Obtén las posiciones del tablero.
        self.set_pieces()  # Coloca las piezas en sus posiciones iniciales.
        #print(self.__board__.show_board())

    def board(self):
        return self.__board__

    def make_piece(self, piece, color, position):
        if piece == "pawn":
            return Pawn(color, position)

        elif piece == "rook":
            return Rook(color, position)

        elif piece == "knight":
            return Knight(color, position)

        elif piece == "bishop":
            return Bishop(color, position)

        elif piece == "queen":
            return Queen(color, position)

        elif piece == "king":
            return King(color, position)
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


if __name__ == "__main__":
    chess = Chess()  # Crea una instancia del juego de ajedrez.
    print(chess.__board__.show_board())  # Imprime el tablero de ajedrez con las piezas colocadas.



