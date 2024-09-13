import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

from .cell import Cell
from .piece import Pieces

class Board:

    def __init__(self):
        self.__positions__ = []
        for row in range(8):  # Itera sobre las filas del tablero (0 a 7).
            self.__positions__.append([])  # Añade una nueva fila como una lista vacía.
            for column in range(8):  # Itera sobre las columnas del tablero (0 a 7).
                # Determina el color de la celda: blanco si la suma de la fila y columna es par, negro si es impar.
                if (row + column) % 2 == 0:
                    color = "white"
                else:
                    color = "black"
                self.__positions__[row].append(Cell(color, (row, column)))  # Añade una celda al tablero con el color correspondiente.

    def get_positions(self):
        return self.__positions__

    def show_board(self, terminal_width=None):
        """
        Renderiza el tablero en formato de texto, mostrando las piezas en sus posiciones actuales.
        Returns:
            str: Una representación en formato de texto del tablero de ajedrez.
        """
        WHITE_BG = '\033[47m'
        BLACK_BG = '\033[40m'
        WHITE_TEXT = '\033[37m'
        BLACK_TEXT = '\033[30m'
        RESET = '\033[0m'

        # Obtener el tamaño de la terminal
        try:
            if terminal_width is None:
                terminal_width = os.get_terminal_size().columns
        except OSError:
            terminal_width = 80  # Valor predeterminado si no es un terminal TTY

        board_width = 8 * 7 + 9
        left_padding = max((terminal_width - board_width) // 2, 0)
        padding = " " * left_padding

        output = padding + "      a      b      c      d      e      f      g      h\n"
        output += padding + "  ┌" + "───────┬" * 7 + "───────┐\n"

        for i, row in enumerate(self.__positions__):
            output += padding + f"{8 - i} │"
            for cell in row:
                piece = cell.get_piece()
                content = f"{piece}" if piece else " "

                cell_color = WHITE_BG if cell.get_color() == "white" else BLACK_BG
                text_color = BLACK_TEXT if cell.get_color() == "white" else WHITE_TEXT

                output += f"{cell_color}{text_color}{content.center(7)}{RESET}│"
            output += f" {8 - i}\n"

            if i < 7:
                output += padding + "  ├" + "───────┼" * 7 + "───────┤\n"
            else:
                output += padding + "  └" + "───────┴" * 7 + "───────┘\n"

        output += padding + "      a      b      c      d      e      f      g      h\n"
        return output

