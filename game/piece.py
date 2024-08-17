class Pieces:
    def __init__(self, color, position):
        self.__color = color
        self.__position = position
        self.__symbol = None

    def move(self, new_position):
        self.__position = new_position

    def valid_moves(self, board):
        raise NotImplementedError("Este método debe ser implementado en subclases.")

    def __repr__(self):
        return self.__symbol if self.__symbol is not None else ""

    def get_color(self):
        return self.__color

    def get_position(self):
        return self.__position

    def get_symbol(self):
        return self.__symbol


class Rook(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)


class Pawn(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
