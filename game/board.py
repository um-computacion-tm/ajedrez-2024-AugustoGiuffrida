import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

from .cell import Cell
from .piece import Pieces

class Board:
    # Constantes para colores ANSI
    WHITE_BG = '\033[47m'  # Fondo blanco
    BLACK_BG = '\033[40m'  # Fondo negro
    WHITE_TEXT = '\033[37m'  # Texto blanco
    BLACK_TEXT = '\033[30m'  # Texto negro
    RESET = '\033[0m'  # Reiniciar color

    def __init__(self):
        # Inicialización del tablero con celdas
        self.__positions__ = [
            [Cell("white" if (row + col) % 2 == 0 else "black", (row, col)) for col in range(8)]
            for row in range(8)
        ]

    def get_positions(self):
        return self.__positions__

    def show_board(self):
        """
        Renderiza el tablero en formato de texto, mostrando las piezas en sus posiciones actuales.
        Returns:
            str: Una representación en formato de texto del tablero de ajedrez.
        """
        # Obtener el tamaño de la terminal
        try:
            terminal_width = os.get_terminal_size().columns
        except OSError:
            terminal_width = 80  # Valor predeterminado si no es un terminal TTY

        # Configuración de formato de tablero
        board_width = 8 * 7 + 9  # 8 celdas de ancho de 7 caracteres cada una + bordes
        left_padding = max((terminal_width - board_width) // 2, 0)
        padding = " " * left_padding

        # Encabezado superior del tablero
        output = padding + "      a      b      c      d      e      f      g      h\n"
        output += padding + "  ┌" + "───────┬" * 7 + "───────┐\n"

        # Construcción de cada fila del tablero
        for i, row in enumerate(self.__positions__):
            output += padding + f"{8 - i} │"
            for cell in row:
                piece = cell.get_piece()  # Obtener la pieza en la celda actual
                content = f"{piece}" if piece else " "

                # Determina el color de la celda y el texto
                cell_color = self.WHITE_BG if cell.get_color() == "white" else self.BLACK_BG
                text_color = self.BLACK_TEXT if cell.get_color() == "white" else self.WHITE_TEXT

                # Añade la celda al tablero
                output += f"{cell_color}{text_color}{content.center(7)}{self.RESET}│"
            output += f" {8 - i}\n"

            # Separador de filas
            if i < 7:
                output += padding + "  ├" + "───────┼" * 7 + "───────┤\n"
            else:
                output += padding + "  └" + "───────┴" * 7 + "───────┘\n"

        # Encabezado inferior del tablero
        output += padding + "      a      b      c      d      e      f      g      h\n"
        return output
