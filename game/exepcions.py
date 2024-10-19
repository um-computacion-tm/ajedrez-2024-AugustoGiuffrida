class InvalidPlay(Exception):
    message = "Invalid piece movement"
    def __str__(self):
        return self.message