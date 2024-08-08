class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = []
        for row in range(8):
            board.append([])
            for col in range(8):
                if (row + col) % 2 == 0:
                    board[row].append(" ")
                else:
                    board[row].append("*")
        return board

    def show_board(self):
        output = "     a     b     c     d     e     f     g     h\n"
        output += "  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐\n"
        
        for i, row in enumerate(self.board):
            output += f"{8 - i} │"
            for square in row:
                output += f"  {square}  │"
            output += f" {8 - i}\n"
            if i < 7:
                output += "  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤\n"
            else:
                output += "  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘\n"
        
        output += "     a     b     c     d     e     f     g     h\n"
        return output

if __name__ == "__main__":
    board = Board()
    print(board.show_board())
