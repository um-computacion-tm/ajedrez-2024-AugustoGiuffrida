class Cell:
    def __init__(self, color, position, content=" "):
        # Verifica que el color sea válido.
        if color not in ["white", "black"]:
            raise ValueError(f"Invalid color: {color}")  # Lanza un error si el color es inválido.
        
        self.__color__ = color  # Asigna el color al atributo privado __color__.
        self.__content__ = content  # Asigna el contenido al atributo privado __content__.
        self.__position__ = position  # Asigna la posición al atributo privado __position__.
        self.__piece__ = None  # Inicializa la pieza en la celda como None (vacío).

    def get_color(self):
        return self.__color__

    def get_position(self):
        return self.__position__

    def get_piece(self):
        return self.__piece__

    def get_content(self):
        return self.__content__

    def __str__(self):
        return self.__content__

    def place_piece(self, piece):
        if self.__piece__ is not None:
            raise ValueError("Cell already occupied")  # Lanza un error si la celda ya está ocupada.
        self.__piece__ = piece  # Coloca la pieza en la celda.

    def remove_piece(self):
        piece = self.__piece__  # Guarda la pieza actual en una variable temporal.
        self.__piece__ = None  # Vacía la celda.
        return piece  # Retorna la pieza removida.

    def is_occupied(self):
        return self.__piece__ is not None  # Retorna True si hay una pieza en la celda, de lo contrario False.
