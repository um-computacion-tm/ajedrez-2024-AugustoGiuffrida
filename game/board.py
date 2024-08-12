import sys
sys.stdout.reconfigure(encoding='utf-8')  # Reconfigura la salida estándar para que utilice la codificación UTF-8.

from .cell import Cell  # Importa la clase Cell desde el módulo cell en el mismo paquete.
from .piece import Pieces  # Importa la clase Pieces desde el módulo piece en el mismo paquete.

class Board:
    """
    Esta clase representa un tablero de ajedrez. Contiene métodos para crear el tablero,
    mostrar las piezas en él y renderizar el tablero en formato de texto.
    """

    def __init__(self):
        """
        Constructor de la clase Board. Inicializa el tablero creando las celdas y 
        colocando las piezas en sus posiciones iniciales.
        """
        self.__board__ = self.create_board()  # Crea el tablero de ajedrez.
        self.show_pieces()  # Coloca las piezas en sus posiciones iniciales.

    def get_board(self):
        """
        Retorna el tablero actual.

        Returns:
            list: El tablero de ajedrez representado como una lista de listas de objetos Cell.
        """
        return self.__board__

    def create_board(self):
        """
        Crea el tablero de ajedrez como una lista de listas de objetos Cell.

        Returns:
            list: Una lista de listas, donde cada sublista representa una fila del tablero,
                  y cada elemento de la sublista es una instancia de la clase Cell.
        """
        board = []  # Inicializa una lista vacía para el tablero.
        for row in range(8):  # Itera sobre las filas del tablero (0 a 7).
            board.append([])  # Añade una nueva fila como una lista vacía.
            for column in range(8):  # Itera sobre las columnas del tablero (0 a 7).
                # Determina el color de la celda: blanco si la suma de la fila y columna es par, negro si es impar.
                if (row + column) % 2 == 0:
                    color = "white" 
                else: 
                    color = "black"
                board[row].append(Cell(color, (row, column)))  # Añade una celda al tablero con el color correspondiente.
        return board  # Retorna el tablero creado.

    def show_board(self):
        """
        Renderiza el tablero en formato de texto, mostrando las piezas en sus posiciones actuales.

        Returns:
            str: Una representación en formato de texto del tablero de ajedrez.
        """
        # Define códigos de colores para las celdas del tablero.
        WHITE_BG = '\033[47m'  # Código ANSI para fondo blanco.
        BLACK_BG = '\033[40m'  # Código ANSI para fondo negro.
        RESET = '\033[0m'  # Código ANSI para reiniciar el color.

        # Encabezado del tablero con las letras de las columnas.
        output = "    a     b     c     d     e     f     g     h\n"
        output += "  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐\n"

        # Itera sobre cada fila del tablero.
        for i, row in enumerate(self.__board__):
            output += f"{8 - i} │"  # Añade el número de fila al inicio de la línea.
            for cell in row:  # Itera sobre cada celda en la fila.
                piece = cell.get_piece()  # Obtiene la pieza en la celda.
                content = f"{piece}" if piece else " "  # Si hay una pieza, se muestra; de lo contrario, muestra un espacio.
                
                # Determina el color de la celda.
                if cell.get_color() == "white":
                    cell_color = WHITE_BG
                else:
                    cell_color = BLACK_BG
                
                # Añade la celda al tablero con el color de fondo correspondiente y el contenido centrado.
                output += f"{cell_color}{content.center(5)}{RESET}│"
            output += f" {8 - i}\n"  # Añade el número de fila al final de la línea.
            if i < 7:
                # Añade una línea divisoria entre filas.
                output += "  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤\n"
            else:
                # Añade la línea final del tablero.
                output += "  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘\n"

        # Añade el encabezado de las columnas nuevamente en la parte inferior.
        output += "    a     b     c     d     e     f     g     h\n"
        return output  # Retorna el tablero en formato de texto.

    def show_pieces(self):
        """
        Coloca las piezas en el tablero utilizando la clase Pieces.
        """
        pieces = Pieces(self.__board__)  # Crea una instancia de la clase Pieces con el tablero actual.
        pieces.set_pieces()  # Coloca las piezas en sus posiciones iniciales.


