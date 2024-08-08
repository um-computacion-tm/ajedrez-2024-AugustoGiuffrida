import unittest
from game.cell import Cell

class TestCell(unittest.TestCase):

    def test_cell_creation_black(self):
        cell = Cell("black")
        self.assertEqual(cell.color, "black")
        self.assertEqual(cell.content, " ")  

    def test_cell_creation_white(self):
        cell = Cell("white")
        self.assertEqual(cell.color, "white")
        self.assertEqual(cell.content, " ")  

    def test_cell_creation_back_with_content(self):
        cell = Cell("black", "p")
        self.assertEqual(cell.color, "black")
        self.assertEqual(cell.content, "p")

    def test_cell_creation_white_with_content(self):
        cell = Cell("white", "p")
        self.assertEqual(cell.color, "white")
        self.assertEqual(cell.content, "p")

    def test_invalid_color(self):          #asegura que el código lance una excepción del tipo ValueError. 
        with self.assertRaises(ValueError):#Si el código no lanza la excepción esperada, el test fallará.
            Cell("blue")                   #Se espera que la clase Cell lance una excepción ValueError 
                                           #porque "blue" no es un color válido

    def test_display_symbol(self):
        self.assertEqual(Cell("black").display_symbol(), "*")
        self.assertEqual(Cell("white").display_symbol(), " ")
                                           
if __name__ == '__main__':
    unittest.main()