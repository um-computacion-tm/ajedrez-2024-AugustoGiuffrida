class Cell:
    """
    La clase Cell representa una celda en un tablero de ajedrez. 
    Cada celda tiene un color, una posición y puede contener una pieza de ajedrez.
    """

    def __init__(self, color, position, content=" "):
        """
        Constructor de la clase Cell.

        Args:
            color (str): El color de la celda, puede ser "white" o "black".
            position (tuple): La posición de la celda en el tablero (fila, columna).
            content (str): El contenido de la celda, por defecto es un espacio en blanco.
        """
        # Verifica que el color sea válido.
        if color not in ["white", "black"]:
            raise ValueError(f"Invalid color: {color}")  # Lanza un error si el color es inválido.
        
        self.__color__ = color  # Asigna el color al atributo privado __color__.
        self.__content__ = content  # Asigna el contenido al atributo privado __content__.
        self.__position__ = position  # Asigna la posición al atributo privado __position__.
        self.__piece__ = None  # Inicializa la pieza en la celda como None (vacío).

    def get_color(self):
        """
        Retorna el color de la celda.

        Returns:
            str: El color de la celda ("white" o "black").
        """
        return self.__color__

    def get_position(self):
        """
        Retorna la posición de la celda en el tablero.

        Returns:
            tuple: La posición de la celda (fila, columna).
        """
        return self.__position__

    def get_piece(self):
        """
        Retorna la pieza contenida en la celda, si la hay.

        Returns:
            str or None: La pieza en la celda o None si está vacía.
        """
        return self.__piece__

    def get_content(self):
        """
        Retorna el contenido de la celda.

        Returns:
            str: El contenido de la celda (por ejemplo, una pieza o un espacio en blanco).
        """
        return self.__content__

    def __str__(self):
        """
        Retorna la representación en cadena del contenido de la celda.

        Returns:
            str: El contenido de la celda.
        """
        return self.__content__

    def place_piece(self, piece):
        """
        Coloca una pieza en la celda.

        Args:
            piece (str): La pieza que se va a colocar en la celda.
        
        Raises:
            ValueError: Si la celda ya está ocupada por otra pieza.
        """
        if self.__piece__ is not None:
            raise ValueError("Cell already occupied")  # Lanza un error si la celda ya está ocupada.
        
        self.__piece__ = piece  # Coloca la pieza en la celda.

    def remove_piece(self):
        """
        Remueve la pieza de la celda y la retorna.

        Returns:
            str or None: La pieza que fue removida o None si la celda estaba vacía.
        """
        piece = self.__piece__  # Guarda la pieza actual en una variable temporal.
        self.__piece__ = None  # Vacía la celda.
        return piece  # Retorna la pieza removida.

    def is_occupied(self):
        """
        Verifica si la celda está ocupada por una pieza.

        Returns:
            bool: True si la celda está ocupada, False en caso contrario.
        """
        return self.__piece__ is not None  # Retorna True si hay una pieza en la celda, de lo contrario False.
