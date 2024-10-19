from .piece import Pawn, Rook, King, Knight, Queen, Bishop
from .piece import Pieces
from .cell import Cell
import os


class Board:

    def __init__(self):
        self.__positions__ = []
        for row in range(8):               # Itera sobre las filas del tablero (0 a 7).
            self.__positions__.append([])  # Añade una nueva fila como una lista vacía.
            for column in range(8):        # Itera sobre las columnas del tablero (0 a 7).
                # Determina el color de la celda: blanco si la suma de la fila y columna es par, negro si es impar.
                if (row + column) % 2 == 0:
                    color = "white"
                else:
                    color = "black"
                self.__positions__[row].append(Cell(color))  # Añade una celda al tablero con el color correspondiente.

    def get_positions(self):
        return self.__positions__

    def get_cell(self, row, col):
        return self.__positions__[row][col]

    def king_in_game(self, color):
        for row in self.__positions__:
            for cell in row:
                piece = cell.get_piece()
                if isinstance(piece, King) and piece.get_color() == color:
                    return True
        return False  

    def orthogonal_move(self, source, dest):
        start, end = sorted((source, dest))
        cells = self.__positions__[start[0]][start[1]+1:end[1]] if start[0] == end[0] else (self.__positions__[i][start[1]] for i in range(start[0]+1, end[0]))
        return all(not cell.is_occupied() for cell in cells)


    def diagonal_move(self, source, dest):
        index_row = 1 if (source[0] - dest[0]) < 0   else -1
        index_col = 1 if (source[1] - dest[1]) < 0   else -1

        # La cantidad de movimientos diagonales (debe ser igual para filas y columnas)
        translation = abs(dest[0] - source[0])

        for i in range(1,translation):
            drow = source[0] + i*index_row
            dcol = source[1] + i*index_col

            if self.__positions__[drow][dcol].is_occupied():
                return False
        return True            
   

    def check_path(self, piece, source, dest):
        move_is_valid = False

        if isinstance(piece, Pawn):
            move_is_valid = piece.valid_moves(source,dest,self)

        elif isinstance(piece, Rook):
            move_is_valid = self.orthogonal_move(source,dest)  # Corregido

        elif isinstance(piece, Knight):
            move_is_valid = piece.valid_moves(source,dest, self)

        elif isinstance(piece, Bishop):
            move_is_valid = self.diagonal_move(source,dest)  # Corregido

        elif isinstance(piece, King):
            # Si el movimiento es ortogonal
            if source[0] == dest[0] or source[1] == dest[1]:
                move_is_valid = self.orthogonal_move(source, dest)  # Corregido
            # Si el movimiento es diagonal
            elif abs(source[0] - dest[0]) == abs(source[1] - dest[1]):
                move_is_valid = self.diagonal_move(source, dest)

        elif isinstance(piece, Queen):
            # Si el movimiento es ortogonal
            if source[0] == dest[0] or source[1] == dest[1]:
                move_is_valid = self.orthogonal_move(source, dest)  # Corregido
            # Si el movimiento es diagonal
            elif abs(source[0] - dest[0]) == abs(source[1] - dest[1]):
                move_is_valid = self.diagonal_move(source, dest)

        return move_is_valid



    def is_valid(self, source, dest):  # -> True/False
        cell = self.__positions__[source[0]][source[1]]
        dest_cell = self.__positions__[dest[0]][dest[1]]
        piece = cell.get_piece()
        
        if piece:
            # Asegúrate de pasar 'self' como el tablero
            if piece.valid_moves(source, dest, self):  # Cambiado aquí
                # Solo permite moverse a una celda ocupada si es una pieza del oponente
                if dest_cell.is_occupied():
                    if dest_cell.get_piece().get_color() != piece.get_color():
                        return self.check_path(piece, source, dest)
                    else:
                        return False  # No puede moverse a una celda ocupada por su propia pieza
                else:
                    return self.check_path(piece, source, dest)
        return False


    def show_board(self, white_captures, black_captures):
        WHITE_BG = '\033[47m'
        BLACK_BG = '\033[40m'
        WHITE_TEXT = '\033[37m'
        BLACK_TEXT = '\033[30m'
        RESET = '\033[0m'

        terminal_width = os.get_terminal_size().columns
        board_width = 8 * 7 + 9
        left_padding = max((terminal_width - board_width) // 2, 0)
        padding = " " * left_padding

        # Piezas capturadas por las negras (mostradas en la parte superior)
        output = padding + "Pieces captured: " + " ".join(str(piece) for piece in black_captures) + "\n"
        output += padding + "      a      b        c       d       e       f       g       h\n"
        output += padding + "  ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐\n"

        for i, row in enumerate(reversed(self.__positions__)):
            output += padding + f"{7 - i} │"
            for cell in row:
                piece = cell.get_piece()

                if piece is not None:
                    content = f"{piece}"
                else:
                    content = " "

                if cell.get_color() == "white":
                    cell_color = WHITE_BG
                    text_color = BLACK_TEXT
                else:
                    cell_color = BLACK_BG
                    text_color = WHITE_TEXT

                output += f"{cell_color}{text_color}{content.center(7)}{RESET}│"
            output += f" {7 - i}\n"
            if i < 7:
                output += padding + "  ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤\n"
            else:
                output += padding + "  └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘\n"

        output += padding + "      a      b        c       d       e       f       g       h\n"
        # Piezas capturadas por las blancas (mostradas en la parte inferior)
        output += padding + "Pieces captured: " + " ".join(str(piece) for piece in white_captures) + "\n"

        return output
        