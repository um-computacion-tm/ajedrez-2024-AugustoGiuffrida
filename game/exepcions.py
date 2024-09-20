class InvalidPlay(Exception):
    message = "Movimieto de pieza invalido"
    def __str__(self):
        return self.message