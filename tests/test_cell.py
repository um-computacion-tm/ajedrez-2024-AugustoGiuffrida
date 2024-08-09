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


    def test_place_piece(self): #Si la pieza en la celda no coincide con la que intentamos colocar         
        cell = Cell("white")    #la prueba fallará
        piece = "Pawn"  
        cell.place_piece(piece)
        self.assertEqual(cell.piece, piece)

    def test_remove_piece(self): 
        cell = Cell("black")
        piece = "Knight"
        cell.place_piece(piece) #El método place_piece debe asignar la pieza a la celda.
        removed_piece = cell.remove_piece() #Se quita la pieza de la celda utilizando el método remove_piece.
        self.assertEqual(removed_piece, piece)#El método debería devolver la pieza que estaba almacenada en la celda antes de quitarla
        self.assertIsNone(cell.piece) #verifica que después de haber quitado la pieza, la celda no contenga ninguna pieza 

    def test_is_occupied(self):
        cell = Cell("white")                #Se verifica que la celda recién creada no esté ocupada. 
        self.assertFalse(cell.is_occupied())#La función is_occupied debería devolver False
        cell.place_piece("Bishop")          #Se coloca una pieza,
        self.assertTrue(cell.is_occupied()) ##La función is_occupied debería devolver True

    def test_place_piece_on_occupied_cell(self):
        cell = Cell("black")
        cell.place_piece("Queen")
        with self.assertRaises(ValueError):#si se intenta colocar una segunda pieza en una celda ocupada, debería lanzar un error
            cell.place_piece("King")       #Se intenta colocar una segunda pieza en la celda que ya está ocupada 
                                           
if __name__ == '__main__':
    unittest.main()