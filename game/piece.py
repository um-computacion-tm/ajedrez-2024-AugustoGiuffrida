from .cell import Cell 


class Pieces:
    def __init__(self, color):
        self.__color__ = color

    def __repr__(self):
        return self.white_repr if self.__color__ == "white" else self.black_repr

    def get_color(self):
        return self.__color__

    def valid_moves_orthogonal(self, old_pos, new_pos):
        return (old_pos[0]==new_pos[0] or old_pos[1]==new_pos[1]) and (old_pos!=new_pos)

    def valid_moves_diagonal(self, old_pos, new_pos):
        return abs(new_pos[0] - old_pos[0]) == abs(new_pos[1] - old_pos[1]) and (old_pos != new_pos)


class Rook(Pieces):
    white_repr = "♖"
    black_repr = "♜"

    def valid_moves(self, old_pos, new_pos):
        return self.valid_moves_orthogonal(old_pos, new_pos)


    
class Bishop(Pieces):
    white_repr = "♗"
    black_repr = "♝"

    def valid_moves(self, old_pos, new_pos):
        return self.valid_moves_diagonal(old_pos, new_pos)



class Knight(Pieces):
    white_repr = "♘"
    black_repr = "♞"

    def valid_moves(self, old_pos, new_pos):
        return self._is_valid_knight_move(old_pos, new_pos)

    def _is_valid_knight_move(self, old_pos, new_pos):
        row_diff = abs(new_pos[0] - old_pos[0])
        col_diff = abs(new_pos[1] - old_pos[1])
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)



class Pawn(Pieces):
    white_repr = "♙"
    black_repr = "♟"

class Pawn(Pieces):
    white_repr = "♙"
    black_repr = "♟"
    
    def valid_moves(self, source, dest):
        direction = 1 if self.get_color() == "white" else -1
        return self._valid_moves(source, dest, direction)
    
    def _valid_moves(self, source, dest, direction):
        forward_move = self._move_forward(source, dest, direction)
        doble_move = self._initial_double_move(source, dest, direction)
        diagonal_cap = self._capture_diagonal(source, dest, direction)
        return forward_move or doble_move or diagonal_cap

    def _move_forward(self, source, dest, direction):
        # Mover una casilla hacia adelante
        return (dest[0] - source[0] == direction) and (source[1] == dest[1])

    def _initial_double_move(self, source, dest, direction):
        # Primer movimiento: puede avanzar dos casillas
        start_row = 1 if direction == 1 else 6
        return (source[0] == start_row) and (dest[0] == source[0] + (2 * direction)) and (source[1] == dest[1])

    def _capture_diagonal(self, source, dest, direction):
        # Captura diagonal
        return (dest[0] - source[0] == direction) and (abs(source[1] - dest[1]) == 1)



class King(Pieces):
    white_repr = "♔"
    black_repr = "♚"

    def valid_moves(self, old_pos, new_pos):
        return abs(old_pos[0]-new_pos[0])<=1 and abs(old_pos[1]-new_pos[1]) <=1 and (old_pos != new_pos)

class Queen(Pieces):
    white_repr = "♕"
    black_repr = "♛"

    def valid_moves(self, old_pos, new_pos):
        return self.valid_moves_orthogonal(old_pos, new_pos) or \
            self.valid_moves_diagonal(old_pos, new_pos)




    