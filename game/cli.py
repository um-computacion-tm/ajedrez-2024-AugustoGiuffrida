from .chess import Chess


class Cli():

    def main(self):
        chess = Chess()
        while chess.is_playing():
            self.play(chess)


    def play(self, chess):

        try:
            print (chess.__board__.show_board())  # Imprime el tablero de ajedrez con las piezas colocadas.
            print ("Turn: ", chess.turn)
            from_row = int(input("From row (0-7): "))
            from_col = int(input("From col (0-7): "))
            to_row = int(input("To row (0-7): "))
            to_col = int(input("To col (0-7): "))
            chess.change_turn()

        except Exception as e:
            return f"error: {e}"


if __name__ == "__main__":
    cli = Cli()
    cli.main()