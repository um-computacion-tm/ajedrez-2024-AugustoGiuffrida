class Cell:
    def __init__(self, color, position=None):  # Modificado para aceptar una posición
        if color not in ["white", "black"]:
            raise ValueError(f"Invalid color: {color}")
        
        self.__color__ = color
        self.__piece__ = None
        self.__position__ = position  # Almacena la posición si se proporciona.

    def get_color(self):
        return self.__color__

    def get_piece(self):
        return self.__piece__

    def get_content(self):
        return str(self.__piece__) if self.__piece__ else " "  # Corregido para devolver un espacio

    def __str__(self):
        return str(self.__piece__) if self.__piece__ else " "

    def place_piece(self, piece):
        self.__piece__ = piece

    def remove_piece(self):
        piece = self.__piece__
        self.__piece__ = None
        return piece

    def is_occupied(self):
        return bool(self.__piece__)
