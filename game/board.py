import sys
sys.stdout.reconfigure(encoding='utf-8')

from .cell import Cell
from .piece import Pieces

class Board:
    def __init__(self):
        self.__board__ = self.create_board()
        self.setup_pieces()

    def get_board(self):
        return self.__board__

    def create_board(self):
        board = []
        for row in range(8):
            board.append([])
            for column in range(8):
                color = "white" if (row + column) % 2 == 0 else "black"
                board[row].append(Cell(color, (row, column)))
        return board

    def show_board(self):
        output = "    a     b     c     d     e     f     g     h\n"
        output += "  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐\n"

        for i, row in enumerate(self.__board__):
            output += f"{8 - i} │"
            for cell in row:
                piece = cell.get_piece()
                if piece:
                    content = f"{piece}".center(5)  # Centramos la pieza en una celda de 5 caracteres
                else:
                    content = " ".center(5)  # Centramos un espacio en una celda de 5 caracteres
                output += f"{content}│"
            output += f" {8 - i}\n"
            if i < 7:
                output += "  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤\n"
            else:
                output += "  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘\n"

        output += "    a     b     c     d     e     f     g     h\n"
        return output

    def setup_pieces(self):
        pieces = Pieces(self.__board__)
        pieces.place_pieces()

if __name__ == "__main__":
    board = Board()
    print(board.show_board())
