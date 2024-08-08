class Cell:
    def __init__(self, color, content=" "):
        if color not in ["white", "black"]:
            raise ValueError(f"Invalid color: {color}")
        self.color = color
        self.content = content

    def __str__(self): #método que se utiliza para representar una instancia de la clase como una cadena de texto
        return self.content# Retorna el contenido de la celda para su visualización
                           #cuando se imprime o converte una celda a una cadena de texto, devuelve el valor almacenado 

    def display_symbol(self):
        # Devuelve el símbolo basado en el color de la celda
        if self.color == "white":
            return " "  # Celda blanca
        else:
            return "*"  # Celda negra

cell = Cell("black", "p")
print(cell)
print (cell.display_symbol())