class Pieces:
    def __init__(self, color, position):
        self.__color__ = color
        self.__position__ = position
        self.__symbol__ = None

    def move(self, new_position):
        self.__position__= new_position

    def valid_moves(self, board):
        raise NotImplementedError("This method should be implemented by subclasses.")    

    def __repr__(self):
        if self.__symbol__:
            return self.__symbol__
        else:
            return "?"      

class Rook(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        if color == "white":
            self.__symbol__ = "♖"
        else:
            self.__symbol__ = "♜"

    def valid_moves(self, board):
        pass
        

class Pawn(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        if color == "white":
            self.__symbol__ = "♙"
        else:
            self.__symbol__ = "♟"

    def valid_moves(self, board):
        pass