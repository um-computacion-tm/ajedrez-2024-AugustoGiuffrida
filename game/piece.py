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

    def valid_moves_vertical(self, board):
        moves = []
        row, column = self.get_position()

        # Movimientos hacia arriba (columna fija, fila decrece)
        for i in range(row - 1, -1, -1):
            cell = board[i][column]
            if cell.is_occupied():
                if cell.get_piece() and cell.get_piece().get_color() != self.get_color():
                    moves.append((i, column))
                break
            moves.append((i, column))

        # Movimientos hacia abajo (columna fija, fila aumenta)
        for i in range(row + 1, 8):
            cell = board[i][column]
            if cell.is_occupied():
                if cell.get_piece() and cell.get_piece().get_color() != self.get_color():
                    moves.append((i, column))
                break
            moves.append((i, column))
        return moves

    def valid_moves_horizontal(self, board):
        moves = []
        row, column = self.get_position()

        # Movimientos hacia la izquierda (fila fija, columna decrece)
        for i in range(column - 1, -1, -1):
            cell = board[row][i]
            if cell.is_occupied():
                if cell.get_piece() and cell.get_piece().get_color() != self.get_color():
                    moves.append((row, i))
                break
            moves.append((row, i))

        # Movimientos hacia la derecha (fila fija, columna aumenta)
        for i in range(column + 1, 8):
            cell = board[row][i]
            if cell.is_occupied():
                if cell.get_piece() and cell.get_piece().get_color() != self.get_color():
                    moves.append((row, i))
                break
            moves.append((row, i))
        return moves

    def valid_moves(self, board):
        return self.valid_moves_vertical(board) + self.valid_moves_horizontal(board)

class Pawn(Pieces):
    def __init__(self, color, position):
        super().__init__(color, position)

    def valid_moves(self, board):
        moves = []
        row, col = self.get_position()

        # Blancas suben, negras bajan
        direction = -1 if self.get_color() == "white" else 1

        # Movimiento hacia adelante
        if board[row + direction][col].get_piece() is None:
            moves.append((row + direction, col))

            # Primer movimiento doble
            if (self.get_color() == "white" and row == 6) or (self.get_color() == "black" and row == 1):
                if board[row + 2 * direction][col].get_piece() is None:
                    moves.append((row + 2 * direction, col))
        return moves