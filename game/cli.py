from .chess import Chess
from .exepcions import InvalidPlay


class Cli:

    def start_game(self):
        chess = Chess()
        while chess.is_playing():
            try:
                print(chess.board.show_board())
                print("Turn: ", chess.turn)
                old_pos = (self.range_input("From row (0-7): "),self.range_input("From col (0-7): "))
                new_pos = (self.range_input("To row (0-7): "),self.range_input("To col (0-7): "))
                chess.play(old_pos,new_pos)
            except InvalidPlay as e:
                print(e)

    def range_input(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if 0 <= value <= 7:
                    return value
                else:
                    print("Las coordenadas están fuera del rango permitido (0-7). Inténtalo de nuevo")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número entre 0 y 7.")

if __name__ == "__main__":
    cli = Cli() 
    # menu = Menu(cli)  # Pasar la instancia de Cli a Menu
    # menu.main()
    cli.start_game()