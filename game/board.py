class Board:
    def __init__(self):
        # Llama al método create_board al crear una instancia de Tablero y guarda el resultado en self.tablero
        self.board = self.create_board()

    def create_board(self):
        board = []  #Inicializa una lista vacía que representará el tablero
        
        for row in range(8): #Recorre 8 filas

            board.append([]) # Añade una lista vacía para cada fila

            for column in range(8):
                if (row + column) % 2 == 0: #Alterna entre espacios claros (" ") y casillas oscuras ("#")
                    board[row].append(" ")
                else:
                    board[row].append("*")
        
        return board #Devuelve el tablero completo

    def show_board(self):
        output = "  a b c d e f g h\n"
        # Recorre cada fila del tablero con su índice
        for i, row in enumerate(self.board):
            output += f"{8 - i} " + " ".join(row) + f" {8 - i}\n"
        output += "  a b c d e f g h"
        return output

if __name__ == "__main__":
    board = Board()  # Crea una instancia de Board
    print(board.show_board())  # Imprime la salida del método show_board en la consola
