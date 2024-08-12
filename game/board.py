import sys
sys.stdout.reconfigure(encoding='utf-8')



from .cell import Cell
from .piece import Pieces


class Board:
    def __init__(self):
        self.__board__ = self.create_board()
        self.show_pieces()

    def get_board(self):
        return self.__board__

    def create_board(self):
        board = []
        for row in range(8):
            board.append([])
            for column in range(8):
                if (row + column) % 2 == 0:
                    color = "white" 
                else: 
                    color = "black"
                board[row].append(Cell(color, (row, column)))
        return board

    def show_board(self):
        # Definimos los códigos de colores ANSI
        WHITE_BG = '\033[47m'
        BLACK_BG = '\033[40m'
        RESET = '\033[0m'

        output = "    a     b     c     d     e     f     g     h\n"
        output += "  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐\n"

        for i, row in enumerate(self.__board__):
            output += f"{8 - i} │"
            for cell in row:
                piece = cell.get_piece()
                content = f"{piece}" if piece else " "
                if cell.get_color() == "white":
                    cell_color = WHITE_BG
                else:
                    cell_color = BLACK_BG
                
                output += f"{cell_color}{content.center(5)}{RESET}│"
            output += f" {8 - i}\n"
            if i < 7:
                output += "  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤\n"
            else:
                output += "  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘\n"

        output += "    a     b     c     d     e     f     g     h\n"
        return output

    def show_pieces(self):
        pieces = Pieces(self.__board__)
        pieces.set_pieces()
        

if __name__ == "__main__":
    board = Board()
    print(board.show_board())
