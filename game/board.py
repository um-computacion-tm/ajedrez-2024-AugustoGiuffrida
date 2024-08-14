import sys
sys.stdout.reconfigure(encoding='utf-8') 

from .cell import Cell 
from .piece import Pieces 

class Board:

    def __init__(self):
        self.__positions__ = []
        for row in range(8):  # Itera sobre las filas del tablero (0 a 7).
            self.__positions__ .append([])  # Añade una nueva fila como una lista vacía.
            for column in range(8):  # Itera sobre las columnas del tablero (0 a 7).
                # Determina el color de la celda: blanco si la suma de la fila y columna es par, negro si es impar.
                if (row + column) % 2 == 0:
                    color = "white" 
                else: 
                    color = "black"
                self.__positions__ [row].append(Cell(color, (row, column)))  # Añade una celda al tablero con el color correspondiente.
        

    def get_positions(self):
        return self.__positions__


    def show_board(self):
        """
        Renderiza el tablero en formato de texto, mostrando las piezas en sus posiciones actuales.

        Returns:
            str: Una representación en formato de texto del tablero de ajedrez.
        """
        WHITE_BG = '\033[47m'  # Código ANSI para fondo blanco.
        BLACK_BG = '\033[40m'  # Código ANSI para fondo negro.
        RESET = '\033[0m'      # Código ANSI para reiniciar el color.

        output = "    a     b     c     d     e     f     g     h\n"
        output += "  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐\n"

        #i: índice de la fila actual en el tablero
        #row: lista que representa una fila del tablero
        for i, row in enumerate(self.__positions__):
            output += f"{8 - i} │"        # Añade el número de fila al inicio de la línea.
            for cell in row:              
                piece = cell.get_piece()  

                # Si hay una pieza, se muestra; de lo contrario, muestra un espacio.
                if piece is not None:  
                    content = f"{piece}" 
                else:
                    content = " "
                
                # Determina el color de la celda.
                if cell.get_color() == "white":
                    cell_color = WHITE_BG
                else:
                    cell_color = BLACK_BG
                
                # Añade la celda al tablero con el color de fondo correspondiente y el contenido centrado.
                output += f"{cell_color}{content.center(5)}{RESET}│"
            output += f" {8 - i}\n"  # Añade el número de fila al final de la línea.
            
            if i < 7:
                output += "  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤\n"
            else:
                output += "  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘\n"

        # Añade el encabezado de las columnas nuevamente en la parte inferior.
        output += "    a     b     c     d     e     f     g     h\n"
        return output  # Retorna el tablero en formato de texto.




