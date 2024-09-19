from .chess import Chess
from .menu import Menu
import os+

class Cli:

    def start_game(self):
        chess = Chess()
        while chess.is_playing():
            self.play(chess)

    def play(self, chess):
        print(chess.__board__.show_board())
        print("Turn: ", chess.turn)
        from_row = self.range_input("From row (0-7): ")
        from_col = self.range_input("From col (0-7): ")
        to_row = self.range_input("To row (0-7): ")
        to_col = self.range_input("To col (0-7): ")
        chess.change_turn()
        os.system('clear')

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
    menu = Menu(cli)  # Pasar la instancia de Cli a Menu
    menu.main()