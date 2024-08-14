from game.board import Board
from game.piece import Pieces

class Chess:

    def __init__(self):
        self.__board__ = Board()  # Inicializa el tablero.
        self.__positions__ = self.__board__.get_positions()  # Obtén las posiciones del tablero.
        self.set_pieces()  # Coloca las piezas en sus posiciones iniciales.
        #print(self.__board__.show_board())

    def get_board(self):
        return self.__board__

    def set_pieces(self):
        # Diccionario que almacena la representación de las piezas de ajedrez con letras minúsculas (blanco) y mayúsculas (negro).
        chess_pieces = {
            "white": {
                "king": "k",
                "queen": "q",
                "rook": "r",
                "bishop": "b",
                "knight": "h",
                "pawn": "p"
            },
            "black": {
                "king": "K",
                "queen": "Q",
                "rook": "R",
                "bishop": "B",
                "knight": "H",
                "pawn": "P"
            }
        }
        # Diccionario alternativo con la representación de las piezas de ajedrez usando símbolos unicode.
        chess_pieces2 = {
            "white": {
                "king": "♔",
                "queen": "♕",
                "rook": "♖",
                "bishop": "♗",
                "knight": "♘",
                "pawn": "♙"
            },
            "black": {
                "king": "♚",
                "queen": "♛",
                "rook": "♜",
                "bishop": "♝",
                "knight": "♞",
                "pawn": "♟"
            }
        }

        # Diccionario que define las posiciones iniciales de las piezas para ambos colores en el tablero.
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
                    if self.__positions__[row][col].is_occupied():
                        raise ValueError(f"Cell at {position} already occupied.")
                    self.__positions__[row][col].place_piece(chess_pieces2[color][piece])

if __name__ == "__main__":
    chess = Chess()  # Crea una instancia del juego de ajedrez.
    print(chess.__board__.show_board())  # Imprime el tablero de ajedrez con las piezas colocadas.



