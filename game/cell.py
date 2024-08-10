class Cell:
    def __init__(self, color, position, content=" "):
        if color not in ["white", "black"]:
            raise ValueError(f"Invalid color: {color}")
        self.__color__ = color
        self.__content__ = content
        self.__position__ = position
        self.__piece__ = None 

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

    def display_symbol(self):
        # Devuelve el símbolo basado en el contenido de la celda, si hay una pieza
        if self.__piece__ is not None:
            return self.__piece__  # Si hay una pieza, muestra el símbolo de la pieza
        return " " if self.__color__ == "white" else "*"  # Muestra el color de la celda si está vacío

    def place_piece(self, piece): 
        if self.__piece__ is not None:
            raise ValueError("Cell already occupied")
        self.__piece__ = piece 

    def remove_piece(self):
        piece = self.__piece__
        self.__piece__ = None
        return piece

    def is_occupied(self):
        return self.__piece__ is not None
