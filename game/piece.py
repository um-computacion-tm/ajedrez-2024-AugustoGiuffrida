import sys
sys.stdout.reconfigure(encoding='utf-8') 

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
    
    def __repr__(self):
        return "♖" if self.get_color() == "white" else "♜"

class Pawn(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
         
    def __repr__(self):
        return "♙" if self.get_color() == "white" else "♟"    

class Bishop(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def __repr__(self):
        return "♗" if self.get_color() == "white" else "♝"

class Knight(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def __repr__(self):
        return "♘" if self.get_color() == "white" else "♞"

class King(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def __repr__(self):
        return "♔" if self.get_color() == "white" else "♚"

class Queen(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def __repr__(self):
        return "♕" if self.get_color() == "white" else "♛"

       
rook_white = Rook("white", "a1")
rook_black = Rook("black", "h8")

print(rook_white)  
print(rook_black)  

# chess_pieces2 = {
#     "white": {
#         "king": "♔",
#         "queen": "♕",
#         "rook": "♖",
#         "bishop": "♗",
#         "knight": "♘",
#         "pawn": "♙"
#     },
#     "black": {
#         "king": "♚",
#         "queen": "♛",
#         "rook": "♜",
#         "bishop": "♝",
#         "knight": "♞",
#         "pawn": "♟"
#     }
# }