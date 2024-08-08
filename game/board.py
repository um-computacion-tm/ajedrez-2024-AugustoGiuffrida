
from .cell import Cell 

class Board:

    def __init__(self):
        self.board = self.create_board()  # Crea el tablero con celdas


    def create_board(self):
        board = []  # Inicializa una lista vacía para el tablero
        for row in range(8):
            board.append([])  # Agrega una nueva fila al tablero
            for column in range(8):
                if (row + column) % 2 == 0: # Determina el color de la celda
                    color = "white" 
                else:
                    color = "black"  
                board[row].append(Cell(color))  # Crea una celda con el color correspondiente
        return board  # Devuelve el tablero completo


    def show_board(self):
        output = "     a     b     c     d     e     f     g     h\n"  # Encabezado de columnas
        output += "  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐\n"  # Línea superior del tablero
        
        for i, row in enumerate(self.board):
            output += f"{8 - i} │"  # Etiqueta de la fila (número de fila)
            for cell in row:
                # Añade el símbolo visual de la celda y las líneas divisorias
                output += f"  {cell.display_symbol()}  │"
            output += f" {8 - i}\n"  # Etiqueta de la fila (número de fila) al final de la línea
            if i < 7:
                output += "  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤\n"
            else:
                output += "  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘\n"  # Línea inferior del tablero
        
        output += "     a     b     c     d     e     f     g     h\n"  # Etiqueta de columnas
        return output  # Devuelve la representación en texto del tablero

if __name__ == "__main__":
    board = Board()  # Crea una instancia del tablero
    print(board.show_board())  # Imprime la representación en texto del tablero




