import os
import sys
from colorama import Fore, Style, init
import tty
import termios

init(autoreset=True)  # Inicializa colorama para resetear colores automáticamente

class Menu:

    def __init__(self, cli):
        self.menu_options = ["Iniciar Juego", "Instrucciones", "Salir"]  # Agregamos la opción de Instrucciones
        self.selected_index = 0
        self.cli = cli

    def main(self):
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

        elif option == "Instrucciones":
            return f"""{color}
██████  ███████  ██████  ██       █████  ███████ 
██   ██ ██      ██       ██      ██   ██ ██      
██████  █████   ██   ███ ██      ███████ ███████ 
██   ██ ██      ██    ██ ██      ██   ██      ██ 
██   ██ ███████  ██████  ███████ ██   ██ ███████ 
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
        elif self.selected_index == 1:  # Opción Instrucciones
            self.show_instructions()
        elif self.selected_index == 2:
            print("Saliendo del juego...")
            exit()

    def show_instructions(self):
        """Muestra las instrucciones del juego y permite regresar al menú."""
        os.system('clear')
        print("=== INSTRUCCIONES ===")
        print("1. El juego termina cuando se captura al rey de tu oponente.")
        print("2. El juego se puede terminar ingreando la palabra 'exit'.")
        print("2. Las piezas blancas están en la parte inferior del tablero y las negras en la parte superior.")
        print("3. Usa las coordenadas del tablero (ej: 'a2' a 'a4') para mover las piezas.")
        print("4. Movimientos de las piezas:")
        print("   - Peones: Se mueven hacia adelante una casilla, o dos casillas desde su posición inicial. Capturan en diagonal.")
        print("   - Torres: Se mueven en línea recta tanto horizontal como verticalmente.")
        print("   - Caballos: Se mueven en forma de 'L', dos casillas en una dirección y una en perpendicular.")
        print("   - Alfiles: Se mueven diagonalmente en cualquier dirección.")
        print("   - Reina: Se mueve en línea recta tanto horizontal como diagonalmente.")
        print("   - Rey: Se mueve una casilla en cualquier dirección.")
        print("\nPresiona cualquier tecla para volver al menú principal.")

        self.get_key()  # Espera a que el usuario presione una tecla para volver al menú
        self.show_start_menu()



    def get_key(self):
        """Obtiene la entrada del teclado sin bloqueo en Linux."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
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
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None