import os
from colorama import Fore, Style, init
import msvcrt  # Importamos msvcrt para capturar entrada de teclado sin bloqueo en Windows
from .chess import Chess

init(autoreset=True)  # Inicializa colorama para resetear colores automáticamente

class Cli:

    def __init__(self):
        self.menu_options = ["Iniciar Juego", "Salir"]
        self.selected_index = 0

    def main(self):
        self.show_start_menu()

    def show_start_menu(self):
        """Muestra el menú de inicio y maneja la entrada del usuario."""
        while True:
            self.display_menu()

            key = msvcrt.getch()  # Captura la entrada del teclado

            if key == b'H':  # Flecha hacia arriba
                self.selected_index = (self.selected_index - 1) % len(self.menu_options)
            elif key == b'P':  # Flecha hacia abajo
                self.selected_index = (self.selected_index + 1) % len(self.menu_options)
            elif key == b'\r':  # Enter
                self.handle_menu_selection()
                break

    def display_menu(self):
        """Muestra el menú con el título y opciones."""
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola
        width = os.get_terminal_size().columns  # Obtiene el ancho de la consola
        self.display_title(width)  # Muestra el título en ASCII Art

        # Mostrar opciones de menú en ASCII Art
        for i, option in enumerate(self.menu_options):
            option_art = self.ascii_option(option, Fore.GREEN if i == self.selected_index else Fore.RESET)
            print(self.center_text(option_art, width))

    def display_title(self, width):
        """Muestra el título 'Ajedrez' usando ASCII Art con colores variados."""
        title_art = [
            f"{Fore.RED} █████╗      ██╗███████╗██████╗ ██████╗ ███████╗███████╗",
            f"{Fore.YELLOW}██╔══██╗     ██║██╔════╝██╔══██╗██╔══██╗██╔════╝╚══███╔╝",
            f"{Fore.GREEN}███████║     ██║█████╗  ██║  ██║██████╔╝█████╗    ███╔╝ ",
            f"{Fore.CYAN}██╔══██║██   ██║██╔══╝  ██║  ██║██╔══██╗██╔══╝   ███╔╝  ",
            f"{Fore.BLUE}██║  ██║╚█████╔╝███████╗██████╔╝██║  ██║███████╗███████╗",
            f"{Fore.MAGENTA}╚═╝  ╚═╝ ╚════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝",
        ]

        # Mostrar cada línea del título centrada
        for line in title_art:
            print(self.center_text(line, width))

    def center_text(self, text, width=80):
        """Centra el texto en el ancho de la consola."""
        lines = text.split('\n')
        centered_lines = [line.center(width) for line in lines]
        return '\n'.join(centered_lines)

    def ascii_option(self, option, color=Fore.RESET):
        """Devuelve el texto de la opción en ASCII Art compacto."""
        if option == "Iniciar Juego":
            return f"""{color}
      _                        
     | |_   _  __ _  __ _ _ __ 
  _  | | | | |/ _` |/ _` | '__|
 | |_| | |_| | (_| | (_| | |   
  \___/ \__,_|\__, |\__,_|_|   
              |___/            
"""

        elif option == "Salir":
            return f"""{color}
  ____        _ _      
 / ___|  __ _| (_)_ __ 
 \___ \ / _` | | | '__|
  ___) | (_| | | | |   
 |____/ \__,_|_|_|_|   
                       
"""

    def handle_menu_selection(self):
        """Maneja la selección del menú según la opción elegida."""
        if self.selected_index == 0:
            self.start_game()
        elif self.selected_index == 1:
            print("Saliendo del juego...")
            exit()

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
    cli.main()
