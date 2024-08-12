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