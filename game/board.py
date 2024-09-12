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

    def show_board(self):
        """
        Renderiza el tablero en formato de texto, mostrando las piezas en sus posiciones actuales.
        Returns:
            str: Una representación en formato de texto del tablero de ajedrez.
        """
        # Códigos ANSI para el color de fondo y el texto.
        WHITE_BG = '\033[47m'  # Fondo blanco
        BLACK_BG = '\033[40m'  # Fondo negro
        WHITE_TEXT = '\033[37m'  # Texto blanco
        BLACK_TEXT = '\033[30m'  # Texto negro
        RESET = '\033[0m'  # Reiniciar color

        # Obtener el tamaño de la terminal
        terminal_width = os.get_terminal_size().columns

        # Tamaño del tablero
        board_width = 8 * 7 + 9  # 8 celdas de ancho de 7 caracteres cada una + bordes

        # Calcular los espacios necesarios para centrar el tablero
        left_padding = max((terminal_width - board_width) // 2, 0)
        padding = " " * left_padding  # Espacios a la izquierda para centrar el tablero

        # Construcción del tablero
        output = padding + "      a      b        c       d       e       f       g       h\n"
        output += padding + "  ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐\n"

        # i: índice de la fila actual en el tablero
        # row: lista que representa una fila del tablero
        for i, row in enumerate(self.__positions__):
            output += padding + f"{8 - i} │"  # Añade el número de fila al inicio de la línea.
            for cell in row:
                piece = cell.get_piece()  # Obtiene la pieza en la celda actual

                # Si hay una pieza, se muestra; de lo contrario, muestra un espacio.
                if piece is not None:
                    content = f"{piece}"
                else:
                    content = " "

                # Determina el color de la celda y el color del texto.
                if cell.get_color() == "white":
                    cell_color = WHITE_BG
                    text_color = BLACK_TEXT  # Texto negro en fondo blanco.
                else:
                    cell_color = BLACK_BG
                    text_color = WHITE_TEXT  # Texto blanco en fondo negro.

                # Añade la celda al tablero con el color de fondo correspondiente y el contenido centrado.
                output += f"{cell_color}{text_color}{content.center(7)}{RESET}│"
            output += f" {8 - i}\n"  # Añade el número de fila al final de la línea.

            if i < 7:
                output += padding + "  ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤\n"
            else:
                output += padding + "  └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘\n"

        # Añade el encabezado de las columnas nuevamente en la parte inferior.
        output += padding + "      a      b        c       d       e       f       g       h\n"
        return output  # Retorna el tablero en formato de texto.
