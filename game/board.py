def show_board(self, terminal_width=None):
    """
    Renderiza el tablero en formato de texto, mostrando las piezas en sus posiciones actuales.
    Returns:
        str: Una representación en formato de texto del tablero de ajedrez.
    """
    WHITE_BG = '\033[47m'
    BLACK_BG = '\033[40m'
    WHITE_TEXT = '\033[37m'
    BLACK_TEXT = '\033[30m'
    RESET = '\033[0m'

    # Obtener el tamaño de la terminal
    try:
        if terminal_width is None:
            terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80  # Valor predeterminado si no es un terminal TTY

    board_width = 8 * 7 + 9
    left_padding = max((terminal_width - board_width) // 2, 0)
    padding = " " * left_padding

    output = padding + "      a      b      c      d      e      f      g      h\n"
    output += padding + "  ┌" + "───────┬" * 7 + "───────┐\n"

    for i, row in enumerate(self.__positions__):
        output += padding + f"{8 - i} │"
        for cell in row:
            piece = cell.get_piece()
            content = f"{piece}" if piece else " "

            cell_color = WHITE_BG if cell.get_color() == "white" else BLACK_BG
            text_color = BLACK_TEXT if cell.get_color() == "white" else WHITE_TEXT

            output += f"{cell_color}{text_color}{content.center(7)}{RESET}│"
        output += f" {8 - i}\n"

        if i < 7:
            output += padding + "  ├" + "───────┼" * 7 + "───────┤\n"
        else:
            output += padding + "  └" + "───────┴" * 7 + "───────┘\n"

    output += padding + "      a      b      c      d      e      f      g      h\n"
    return output
