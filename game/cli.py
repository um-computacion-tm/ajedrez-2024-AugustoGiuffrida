from .chess import Chess


class Cli():

    def main(self):
        chess = Chess()
        while chess.is_playing():
            self.play(chess)

# print (chess.__board__.show_board())  
# print ("Turn: ", chess.turn)
# from_row = int(input("From row (0-7): "))
# from_col = int(input("From col (0-7): "))
# to_row = int(input("To row (0-7): "))
# to_col = int(input("To col (0-7): "))

# if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
#     raise ValueError("Las coordenadas están fuera del rango permitido (0-7)")


    def play(self, chess):

        try:
            print(chess.__board__.show_board())  
            print("Turn: ", chess.turn)

            # fila de origen
            while True:
                from_row = int(input("From row (0-7): "))
                if 0 <= from_row <= 7:
                    break
                else:
                    print("Error: El valor debe estar entre 0 y 7.")

            # columna de origen
            while True:
                from_col = int(input("From col (0-7): "))
                if 0 <= from_col <= 7:
                    break
                else:
                    print("Error: El valor debe estar entre 0 y 7.")

            # fila de destino
            while True:
                to_row = int(input("To row (0-7): "))
                if 0 <= to_row <= 7:
                    break
                else:
                    print("Error: El valor debe estar entre 0 y 7.")

            # columna de destino
            while True:
                to_col = int(input("To col (0-7): "))
                if 0 <= to_col <= 7:
                    break
                else:
                    print("Error: El valor debe estar entre 0 y 7.")

            chess.change_turn()


        except ValueError as ve:
            return f"Error: {ve}"

        except Exception as e:
            return f"Error: {e}"


if __name__ == "__main__":
    Cli().main()
    