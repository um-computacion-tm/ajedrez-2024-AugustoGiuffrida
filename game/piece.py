from .cell import Cell 
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


class Rook(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.white_repr = "♖"
        self.black_repr = "♜"

    def valid_moves(self, board):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (fila, columna)
        row, col = self.get_position()

        for dr, dc in directions:
            for i in range(1,8):
                new_row, new_col = row + i*dr, col + i*dc
                if 0<= new_row <=7 and 0<= new_col <=7:
                    cell = board[new_row][new_col]   
                    if cell.is_occupied():
                        if cell.get_piece().get_color() != self.get_color():
                            moves.append((new_row,new_col))
                        break
                    moves.append((new_row,new_col))
                else:
                    break 
        return moves  


class Bishop(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.white_repr = "♗"
        self.black_repr = "♝"

    def valid_moves(self, board):
        moves = []
        directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]  # Arriba-Derecha, Arriba-Izquierda, Abajo-Derecha, Abajo-Izquierda
        row, col = self.get_position() 

        for dr, dc in directions:
            for i in range(1,8):
                new_row, new_col = row + i*dr, col + i*dc
                if 0<= new_row <=7 and 0<= new_col <=7:
                    cell = board[new_row][new_col]   
                    if cell.is_occupied():
                        if cell.get_piece().get_color() != self.get_color():
                            moves.append((new_row,new_col))
                        break
                    moves.append((new_row,new_col))
                else:
                    break 
        return moves         

class Pawn(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.white_repr = "♙"
        self.black_repr = "♟"

class Knight(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.white_repr = "♘"
        self.black_repr = "♞"

class King(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.white_repr = "♔"
        self.black_repr = "♚"

class Queen(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.white_repr = "♕"
        self.black_repr = "♛"

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