class InvalidPlay(Exception):
    message = "Movimiento de pieza invalido"
    def __str__(self):
        return self.message