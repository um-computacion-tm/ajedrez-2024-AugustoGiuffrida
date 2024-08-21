class Pieces:
    def __init__(self, color, position):
        self.__color__ = color
        self.__position__ = position
        self.__symbol__ = None

    def move(self, new_position, board):
        if new_position in self.valid_moves(board):
            self.__position__ = new_position
        else:
            raise ValueError("Movimiento no válido.")

    def valid_moves(self, board):
        raise NotImplementedError("Este método debe ser implementado en subclases.")

    def __repr__(self):
        return self.__symbol__ if self.__symbol__ is not None else ""

    def get_color(self):
        return self.__color__

    def get_position(self):
        return self.__position__

    def get_symbol(self):
        return self.__symbol__

class Rook(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)


class Pawn(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
