import os
import sys
from colorama import Fore, Style, init
import tty
import termios

init(autoreset=True)  # Inicializa colorama para resetear colores automáticamente

class  Menu:
    def __init__(self, cli):
        self.menu_options = ["Iniciar Juego", "Salir"]
        self.selected_index = 0
        self.cli = cli

    def main(self):
        parser = argparse.ArgumentParser(description='Ajedrez CLI')
        parser.add_argument('--no-menu', action='store_true', help='Ejecuta la opción predeterminada sin mostrar el menú')
        args = parser.parse_args()

        # Si no es un terminal interactivo, ejecutar la opción predeterminada
        if not sys.stdin.isatty() or args.no_menu:
            self.cli.start_game()
        else:
            self.show_start_menu()

    def show_start_menu(self):
        """Muestra el menú de inicio y maneja la entrada del usuario."""
        while True:
            self.display_menu()

            key = self.get_key()  # Captura la entrada del teclado

            if key == 'up':  # Flecha hacia arriba
                self.selected_index = (self.selected_index - 1) % len(self.menu_options)
            elif key == 'down':  # Flecha hacia abajo
                self.selected_index = (self.selected_index + 1) % len(self.menu_options)
            elif key == 'enter':  # Enter
                self.handle_menu_selection()
                break

    def display_menu(self):
        """Muestra el menú con el título y opciones."""
        os.system('clear')  # Limpia la consola en Linux
        try:
            width = os.get_terminal_size().columns  # Obtiene el ancho de la consola
        except OSError:
            width = 80  # Valor predeterminado si no se puede obtener el tamaño de la terminal

        self.display_title(width)  # Muestra el título en ASCII Art

        # Mostrar opciones de menú en ASCII Art
        for i, option in enumerate(self.menu_options):
            option_art = self.ascii_option(option, Fore.GREEN if i == self.selected_index else Fore.RESET)
            print(self.center_text(option_art, width))

    def display_title(self, width):
        """Muestra el título 'Ajedrez' usando ASCII Art con colores variados."""
        title_art = [
            f"{Fore.RED}      █████╗      ██╗███████╗██████╗ ██████╗ ███████╗███████╗",
            f"{Fore.YELLOW}     ██╔══██╗     ██║██╔════╝██╔══██╗██╔══██╗██╔════╝╚══███╔╝",
            f"{Fore.GREEN}     ███████║     ██║█████╗  ██║  ██║██████╔╝█████╗    ███╔╝ ",
            f"{Fore.CYAN}     ██╔══██║██   ██║██╔══╝  ██║  ██║██╔══██╗██╔══╝   ███╔╝  ",
            f"{Fore.BLUE}     ██║  ██║╚█████╔╝███████╗██████╔╝██║  ██║███████╗███████╗",
            f"{Fore.MAGENTA}     ╚═╝  ╚═╝ ╚════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝",
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

     ██ ██    ██  ██████   █████  ██████  
     ██ ██    ██ ██       ██   ██ ██   ██ 
     ██ ██    ██ ██   ███ ███████ ██████  
██   ██ ██    ██ ██    ██ ██   ██ ██   ██ 
 █████   ██████   ██████  ██   ██ ██   ██ 
                                          
                                          

"""

        elif option == "Salir":
            return f"""{color}

███████  █████  ██      ██ ██████  
██      ██   ██ ██      ██ ██   ██ 
███████ ███████ ██      ██ ██████  
     ██ ██   ██ ██      ██ ██   ██ 
███████ ██   ██ ███████ ██ ██   ██ 
                                   
                                   

"""

    def handle_menu_selection(self):
        """Maneja la selección del menú según la opción elegida."""
        if self.selected_index == 0:
            os.system('clear')
            self.cli.start_game()
        elif self.selected_index == 1:
            print("Saliendo del juego...")
            exit()


    def get_key(self):
        """Obtiene la entrada del teclado sin bloqueo en Linux."""
        if not sys.stdin.isatty():
            # Si no es un TTY, devuelve 'enter' o alguna opción predeterminada
            print("Advertencia: No se puede capturar la entrada del teclado en un entorno no interactivo.")
            return 'enter'  # O la opción que prefieras

        try:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            tty.setraw(sys.stdin.fileno())
            key = sys.stdin.read(1)
            if key == '\x1b':  # Secuencia de escape de teclas
                next_key = sys.stdin.read(1)
                if next_key == '[':  # Comienza secuencia de flechas
                    arrow_key = sys.stdin.read(1)
                    if arrow_key == 'A':
                        return 'up'
                    elif arrow_key == 'B':
                        return 'down'
            elif key == '\r' or key == '\n':  # Enter puede ser '\r' o '\n'
                return 'enter'
        except termios.error as e:
            print(f"Error de terminal: {e}")
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None

