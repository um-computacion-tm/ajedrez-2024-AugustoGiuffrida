from .chess import Chess
from .exepcions import InvalidPlay
#
# from .menu import Menu

class Cli:

    def start_game(self):
        chess = Chess()
        while chess.is_playing():
            try:
                print(chess.board.show_board())
                print("Turn: ", chess.turn)
                old_pos = (self.validate_input("Enter initial position (e.g 'a2'): "))
                new_pos = (self.validate_input("Enter final position (e.g 'a3'): "))
                chess.play(old_pos,new_pos)
            except InvalidPlay as e:
                print(e)

    def validate_input(self, prompt):
        while True: 
            position = input(prompt).lower().replace(" ", "")
            converted_position = self.convert_position(position)
            if converted_position:  
                return converted_position


    def convert_position(self, position):
        # Listas de columnas y filas
        columns = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        rows = ('0', '1', '2', '3', '4', '5', '6', '7')

        # Verifica que la longitud de la posición sea de 2 caracteres
        if len(position) != 2:
            print("\nInvalid input length.\n")
            return False

        try:
           
            new_column, new_row = position[0], position[1]

            if new_column not in columns or new_row not in rows:
                print("\nInvalid column or row value.\n")
                return False

            # Convertimos los caracteres en índices de tuplas
            r = rows.index(new_row)
            c = columns.index(new_column)

            return (r, c)

        except (ValueError, IndexError):
            print("\nInvalid input.\n")
            return False



if __name__ == "__main__":
    cli = Cli() 
    # menu = Menu(cli)  # Pasar la instancia de Cli a Menu
    # menu.main()
    cli.start_game()