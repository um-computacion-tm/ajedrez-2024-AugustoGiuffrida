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
        print("  a b c d e f g h")
        #Recorre cada fila del tablero con su índice
        for i, row in enumerate(self.board): #enumerate: función que devuelve el índice y el elemento para cada iteración sobre self.tablero

            print(8 - i, end=" ") #Imprime el número de fila (de 8 a 1) seguido de un espacio
            
            for square in row: #Recorre cada casilla de la fila e imprime su contenido seguido de un espacio
                
                print(square, end=" ")
            
            print(8 - i) #Imprime el número de fila al final de la fila y salta a la siguiente línea
      
        print("  a b c d e f g h")

if __name__ == "__main__":
    
    board = Board() #Crea una instancia de Tablero
    
    board.show_board() #Llama al método show_board para imprimir el tablero en la consola
