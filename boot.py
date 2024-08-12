# run_board.py

from game.board import Board


# Código para ejecutar la clase Board si este archivo se ejecuta como un script.
if __name__ == "__main__":
    board = Board()  # Crea una instancia del tablero de ajedrez.
    print(board.show_board())  # Imprime el tablero de ajedrez en formato de texto.

#python boot.py
