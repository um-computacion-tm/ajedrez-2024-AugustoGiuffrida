from .cell import Cell 
import sys
sys.stdout.reconfigure(encoding='utf-8')

class Pieces:
    def __init__(self, color, position):
        self.__color__ = color
        self.__position__ = position

    def __repr__(self):
        return self.white_repr if self.__color__ == "white" else self.black_repr

    def get_color(self):
        return self.__color__

    def get_position(self):
        return self.__position__


class Rook(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.white_repr = "♖"
        self.black_repr = "♜"

    def valid_moves_vertical(self, board):
        moves = []
        row, col = self.get_position() 

        #Movimientos hacia arriba (columna fija, fila decrece)
        for i in range (row-1,-1,-1):
            cell = board[i][col]
            if cell.is_occupied():
                if cell.get_piece().get_color() != self.get_color(): 
                    moves.append((i,col))                            
                break
            moves.append((i, col))

        #Movimientos hacia abajo (columna fija, fila aumenta)
        for i in range (row+1,8):
            cell = board[i][col]
            if cell.is_occupied():
                if cell.get_piece().get_color() != self.get_color():
                    moves.append((i,col))                       
                break
            moves.append((i, col))    


    def valid_moves_horizontal(self, board):
        moves = []
        row, col = self.get_position() 

        #Movimientos hacia la izquierda (fila fija, columna decrece)
        for i in range (col-1,-1,-1):
            cell = board[row][i]
            if cell.is_occupied():
                if cell.get_piece().get_color() != self.get_color(): 
                    moves.append((row,i))                       
                break
            moves.append((row, i))

        #Movimientos hacia la derecha (fila fija, columna aumenta)
        for i in range(col + 1, 8):
            cell = board[row][i]
            if cell.is_occupied():
                if cell.get_piece().get_color() != self.get_color():
                    moves.append((row, i))
                break
            moves.append((row, i))   
        return moves   


class Bishop(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.white_repr = "♗"
        self.black_repr = "♝"

    def valid_moves_asc(self, board):
        moves = []
        row, col = self.get_position() 

        #Movimientos hacia arriba y la derecha 
        for i in range(1,8):
            new_row, new_col = row - i, col + i
            if 0<= new_row <=7 and 0<= new_col <=7:
                cell = board[new_row][new_col]   
                if cell.is_occupied():
                    if cell.get_piece().get_color() != self.get_color:
                        moves.append((new_row,new_col))
                    break
                moves.append((new_row,new_col))
            else:
                break  

        #Movimientos hacia arriba y la izquierda 
        for i in range(1,8):
            new_row, new_col = row - i, col - i
            if 0<= new_row <=7 and 0<= new_col <=7:
                cell = board[new_row][new_col]   
                if cell.is_occupied():
                    if cell.get_piece().get_color() != self.get_color:
                        moves.append((new_row,new_col))
                    break
                moves.append((new_row,new_col))
            else:
                break  


    def valid_moves_desc(self, board):
        moves = []
        row, col = self.get_position() 

        #Movimientos hacia abajo y la derecha 
        for i in range(1,8):
            new_row, new_col = row + i, col + i
            if 0<= new_row <=7 and 0<= new_col <=7:
                cell = board[new_row][new_col]   
                if cell.is_occupied():
                    if cell.get_piece().get_color() != self.get_color:
                        moves.append((new_row,new_col))
                    break
                moves.append((new_row,new_col))
            else:
                break  

        #Movimientos hacia abajo y la izquierda 
        for i in range(1,8):
            new_row, new_col = row + i, col - i
            if 0<= new_row <=7 and 0<= new_col <=7:
                cell = board[new_row][new_col]   
                if cell.is_occupied():
                    if cell.get_piece().get_color() != self.get_color:
                        moves.append((new_row,new_col))
                    break
                moves.append((new_row,new_col))
            else:
                break            


class Pawn(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.white_repr = "♙"
        self.black_repr = "♟"

class Knight(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.white_repr = "♘"
        self.black_repr = "♞"

class King(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.white_repr = "♔"
        self.black_repr = "♚"

class Queen(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.white_repr = "♕"
        self.black_repr = "♛"


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