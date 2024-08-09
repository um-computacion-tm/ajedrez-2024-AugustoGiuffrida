class Cell:
    def __init__(self, color, content=" "):
        if color not in ["white", "black"]:
            raise ValueError(f"Invalid color: {color}")
        self.color = color
        self.content = content
        self.piece = None 

    def __str__(self): #-->método que se utiliza para representar una instancia de la clase como una cadena de texto
        return self.content# Retorna el contenido de la celda para su visualización
                           #cuando se imprime o converte una celda a una cadena de texto, devuelve el valor almacenado 

    def display_symbol(self):
        # Devuelve el símbolo basado en el color de la celda
        if self.color == "white":
            return " "  # Celda blanca
        else:
            return "*"  # Celda negra

    def place_piece(self, piece): #-->coloca una pieza en la celda actual
        if self.piece is not None:#si self.piece no es None, significa que hay una pieza, no se puede poner otra pieza en esa celda.
            raise ValueError("Cell already occupied")#indica que no se puede colocar una nueva pieza porque la celda ya está ocupada
        self.piece = piece #permite colocar la nueva pieza.

    def remove_piece(self):
        piece = self.piece #guarda la pieza que está en la celda (self.piece) en la variable piece.
        self.piece = None  #la celda se "vacía" estableciendo self.piece a None
        return piece

    def is_occupied(self):#-->verifica si la celda ya tiene una pieza
        return self.piece is not None #Si hay una pieza (self.piece no es None), la función devuelve True. 
                                      #Si no hay ninguna pieza en la celda (self.piece es None), devuelve False

#cell = Cell("black", "p")
#print(cell)
#print (cell.display_symbol())