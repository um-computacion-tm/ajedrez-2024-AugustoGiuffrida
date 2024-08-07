class Tablero:
    def __init__(self):
        # Llama al método crear_tablero al crear una instancia de Tablero y guarda el resultado en self.tablero
        self.tablero = self.crear_tablero()

    def crear_tablero(self):
        tablero = []  #Inicializa una lista vacía que representará el tablero
        
        for fila in range(8): #Recorre 8 filas

            tablero.append([])  

            for columna in range(8):
                if (fila + columna) % 2 == 0: #Alterna entre espacios claros (" ") y casillas oscuras ("#")
                    tablero[fila].append(" ")
                else:
                    tablero[fila].append("#")
        
        return tablero #Devuelve el tablero completo

    def mostrar(self):
        print("  a b c d e f g h")
        #Recorre cada fila del tablero con su índice
        for i, fila in enumerate(self.tablero): #enumerate: función que devuelve el índice y el elemento para cada iteración sobre self.tablero

            print(8 - i, end=" ") #Imprime el número de fila (de 8 a 1) seguido de un espacio
            
            for casilla in fila: #Recorre cada casilla de la fila e imprime su contenido seguido de un espacio
                
                print(casilla, end=" ")
            
            print(8 - i) #Imprime el número de fila al final de la fila y salta a la siguiente línea
      
        print("  a b c d e f g h")

if __name__ == "__main__":
    
    tablero = Tablero() #Crea una instancia de Tablero
    
    tablero.mostrar() #Llama al método mostrar para imprimir el tablero en la consola
