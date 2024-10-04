import unittest
from game.cell import Cell

class TestCell(unittest.TestCase):

    def test_cell_creation_black(self):
        cell = Cell("black")
        self.assertEqual(cell.get_color(), "black")
        self.assertEqual(cell.get_content(), " ")  # Debe estar vacío

    def test_cell_creation_white(self):
        cell = Cell("white")
        self.assertEqual(cell.get_color(), "white")
        self.assertEqual(cell.get_content(), " ")  # Debe estar vacío

    def test_invalid_color(self):
        with self.assertRaises(ValueError):
            Cell("blue")  # Color no válido

    def test_place_piece(self):
        cell = Cell("white")
        piece = "Pawn"
        cell.place_piece(piece)
        self.assertEqual(cell.get_piece(), piece)

    def test_remove_piece(self):
        cell = Cell("black")
        piece = "Knight"
        cell.place_piece(piece)
        removed_piece = cell.remove_piece()
        self.assertEqual(removed_piece, piece)
        self.assertIsNone(cell.get_piece())

    def test_is_occupied(self):
        cell = Cell("white")
        self.assertFalse(cell.is_occupied())
        cell.place_piece("Bishop")
        self.assertTrue(cell.is_occupied())


    def test_str_method(self):
        cell = Cell("white")
        self.assertEqual(str(cell), " ")  # Celda vacía
        cell.place_piece("p")
        self.assertEqual(str(cell), "p")  # Debe mostrar la pieza

if __name__ == '__main__':
    unittest.main()
