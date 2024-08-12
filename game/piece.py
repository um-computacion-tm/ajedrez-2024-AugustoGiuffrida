class Pieces:
    """
    La clase Pieces se encarga de manejar las piezas en el tablero de ajedrez. 
    Incluye métodos para establecer las posiciones iniciales de las piezas.
    """

    def __init__(self, board):
        """
        Constructor de la clase Pieces.

        Args:
            board (list): El tablero de ajedrez, representado como una lista de listas de objetos Cell.
        """
        self.__board__ = board  # Asigna el tablero proporcionado al atributo privado __board__.

    def set_pieces(self):
        """
        Coloca las piezas de ajedrez en sus posiciones iniciales en el tablero.
        """

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
                "rook": [(7, 0), (7, 7)],  # Posiciones iniciales de las torres blancas.
                "knight": [(7, 1), (7, 6)],  # Posiciones iniciales de los caballos blancos.
                "bishop": [(7, 2), (7, 5)],  # Posiciones iniciales de los alfiles blancos.
                "queen": [(7, 3)],  # Posición inicial de la reina blanca.
                "king": [(7, 4)],  # Posición inicial del rey blanco.
                "pawn": [(6, i) for i in range(8)]  # Posiciones iniciales de los peones blancos.
            },
            "black": {
                "rook": [(0, 0), (0, 7)],  # Posiciones iniciales de las torres negras.
                "knight": [(0, 1), (0, 6)],  # Posiciones iniciales de los caballos negros.
                "bishop": [(0, 2), (0, 5)],  # Posiciones iniciales de los alfiles negros.
                "queen": [(0, 3)],  # Posición inicial de la reina negra.
                "king": [(0, 4)],  # Posición inicial del rey negro.
                "pawn": [(1, i) for i in range(8)]  # Posiciones iniciales de los peones negros.
            }
        }

        for color, pieces in initial_positions.items(): #-->Devuelve un par iterable (clave, valor), pieces: diccionario
            for piece, positions in pieces.items(): #positions: lista de tuplas
                for position in positions: #position: tupla
                    row, col = position
                    if self.__board__[row][col].is_occupied(): # Verifica si la celda ya está ocupada antes de colocar la pieza
                        raise ValueError(f"Cell at {position} already occupied.")
                    self.__board__[row][col].place_piece(chess_pieces[color][piece])
