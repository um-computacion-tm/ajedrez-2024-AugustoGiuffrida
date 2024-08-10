class Pieces:
    def __init__(self, board):
        self.__board__ = board

    def place_pieces(self):
       
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
       
        chess_pieces2= {
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

        initial_positions = {
            "white": {
                "rook": [(0,0),(0,7)],
                "knight": [(0,1),(0,6)],
                "bishop": [(0,2),(0,5)],
                "queen": [(0,3)],
                "king": [(0,4)],
                "pawn": [(1,i) for i in range(8)]
            },
            "black": {
                "rook": [(7,0),(7,7)],
                "knight": [(7,1),(7,6)],
                "bishop": [(7,2),(7,5)],
                "queen": [(7,3)],
                "king": [(7,4)],
                "pawn": [(6,i) for i in range(8)]
            }
        }

        for color, pieces in initial_positions.items():
            for piece, positions in pieces.items():
                for position in positions:
                    row, col = position
                    # Verifica si la celda ya está ocupada antes de colocar la pieza
                    if self.__board__[row][col].is_occupied():
                        raise ValueError(f"Cell at {position} already occupied.")
                    self.__board__[row][col].place_piece(chess_pieces[color][piece])
