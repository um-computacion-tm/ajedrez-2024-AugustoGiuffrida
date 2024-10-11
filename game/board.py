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

    def orthogonal_move(self, source, dest):
        # Si el movimiento es horizontal entonces index = 1
        index = 1 if source[0] == dest[0] else 0
        mov = dest[index]-source[index]
        translation = mov if mov>0 else -mov
        sign = 1 if mov>0 else -1
        for i in range(1,translation,sign):
            if self.__positions__[dest[0] if index else i][i if index else dest[1]].is_occupied():
                return False
        return True

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
            move_is_valid = piece.valid_moves(source,dest)

        elif isinstance(piece, Rook):
            move_is_valid = self.orthogonal_move(source,dest)

        elif isinstance(piece, Knight):
            move_is_valid = piece.valid_moves(source,dest)

        elif isinstance(piece, Bishop):
            move_is_valid = self.diagonal_move(source,dest)
            
        elif isinstance(piece, King):
            # Si el movimiento es ortogonal
            if source[0] == dest[0] or source[1] == dest[1]:
                move_is_valid = self.orthogonal_move(source, dest)
            # Si el movimiento es diagonal
            elif abs(source[0] - dest[0]) == abs(source[1] - dest[1]):
                move_is_valid =self.diagonal_move(source, dest)
                
        elif isinstance(piece, Queen):
            # Si el movimiento es ortogonal
            if source[0] == dest[0] or source[1] == dest[1]:
                move_is_valid = self.orthogonal_move(source, dest)
            # Si el movimiento es diagonal
            elif abs(source[0] - dest[0]) == abs(source[1] - dest[1]):
                move_is_valid = self.diagonal_move(source, dest)

        return move_is_valid 


    def is_valid(self, source, dest): # -> True/False
        # Buscamos la celda y la pieza a validar
        cell = self.__positions__[source[0]][source[1]]
        dest_cell = self.__positions__[dest[0]][dest[1]]
        piece = cell.get_piece()
        if piece.valid_moves(source, dest):
            if dest_cell.is_occupied():
                if dest_cell.get_piece().get_color() != piece.get_color():
                    return self.check_path(piece, source, dest)
            else:
                return self.check_path(piece, source, dest)
        return False

    def show_board(self):
        output = "    a     b     c     d     e     f     g     h\n"
        output += "  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐\n"

        # Invertir las filas al mostrar el tablero
        for i, row in enumerate(reversed(self.__positions__)):
            output += f"{7 - i} │"
            for cell in row:
                piece = cell.get_piece()
                if piece:
                    content = f"{piece}".center(5)  # Centramos la pieza en una celda de 5 caracteres
                else:
                    content = " ".center(5)  # Centramos un espacio en una celda de 5 caracteres
                output += f"{content}│"
            output += f" {7 - i}\n"
            if i < 7:
                output += "  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤\n"
            else:
                output += "  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘\n"

        output += "    a     b     c     d     e     f     g     h\n"
        return output


    # def show_board(self):
    #     """
    #     Renderiza el tablero en formato de texto, mostrando las piezas en sus posiciones actuales.
    #     Returns:
    #         str: Una representación en formato de texto del tablero de ajedrez.
    #     """
    #     # Códigos ANSI para el color de fondo y el texto.
    #     WHITE_BG = '\033[47m'  # Fondo blanco
    #     BLACK_BG = '\033[40m'  # Fondo negro
    #     WHITE_TEXT = '\033[37m'  # Texto blanco
    #     BLACK_TEXT = '\033[30m'  # Texto negro
    #     RESET = '\033[0m'  # Reiniciar color

    #     # Obtener el tamaño de la terminal
    #     terminal_width = os.get_terminal_size().columns

    #     # Tamaño del tablero
    #     board_width = 8 * 7 + 9  # 8 celdas de ancho de 7 caracteres cada una + bordes

    #     # Calcular los espacios necesarios para centrar el tablero
    #     left_padding = max((terminal_width - board_width) // 2, 0)
    #     padding = " " * left_padding  # Espacios a la izquierda para centrar el tablero

    #     # Construcción del tablero
    #     output = padding + "      a      b        c       d       e       f       g       h\n"
    #     output += padding + "  ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐\n"

    #     # i: índice de la fila actual en el tablero
    #     # row: lista que representa una fila del tablero
    #     for i, row in enumerate(reversed(self.__positions__)):
    #         output += padding + f"{7 - i} │"  # Añade el número de fila al inicio de la línea.
    #         for cell in row:
    #             piece = cell.get_piece()  # Obtiene la pieza en la celda actual

    #             # Si hay una pieza, se muestra; de lo contrario, muestra un espacio.
    #             if piece is not None:
    #                 content = f"{piece}"
    #             else:
    #                 content = " "

    #             # Determina el color de la celda y el color del texto.
    #             if cell.get_color() == "white":
    #                 cell_color = WHITE_BG
    #                 text_color = BLACK_TEXT  # Texto negro en fondo blanco.
    #             else:
    #                 cell_color = BLACK_BG
    #                 text_color = WHITE_TEXT  # Texto blanco en fondo negro.

    #             # Añade la celda al tablero con el color de fondo correspondiente y el contenido centrado.
    #             output += f"{cell_color}{text_color}{content.center(7)}{RESET}│"
    #         output += f" {7 - i}\n"  # Añade el número de fila al final de la línea.

    #         if i < 7:
    #             output += padding + "  ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤\n"
    #         else:
    #             output += padding + "  └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘\n"

    #     # Añade el encabezado de las columnas nuevamente en la parte inferior.
    #     output += padding + "      a      b        c       d       e       f       g       h\n"
    #     return output  # Retorna el tablero en formato de texto.
        
