import unittest
from game.cell import Cell

class TestCell(unittest.TestCase):

    def test_cell_creation_black(self):
        cell = Cell("black", (0, 0))
        self.assertEqual(cell.get_color(), "black")
        self.assertEqual(cell.get_content(), " ")

    def test_cell_creation_white(self):
        cell = Cell("white", (0, 0))
        self.assertEqual(cell.get_color(), "white")
        self.assertEqual(cell.get_content(), " ")

    def test_cell_creation_black_with_content(self):
        cell = Cell("black", (0, 0), "p")
        self.assertEqual(cell.get_color(), "black")
        self.assertEqual(cell.get_content(), "p")

    def test_cell_creation_white_with_content(self):
        cell = Cell("white", (0, 0), "p")
        self.assertEqual(cell.get_color(), "white")
        self.assertEqual(cell.get_content(), "p")

    def test_invalid_color(self):
        with self.assertRaises(ValueError):
            Cell("blue", (0, 0))

    def test_display_symbol(self):
        self.assertEqual(Cell("black", (0, 0)).display_symbol(), "*")
        self.assertEqual(Cell("white", (0, 0)).display_symbol(), " ")

    def test_place_piece(self):
        cell = Cell("white", (0, 0))
        piece = "Pawn"
        cell.place_piece(piece)
        self.assertEqual(cell.get_piece(), piece)

    def test_remove_piece(self):
        cell = Cell("black", (0, 0))
        piece = "Knight"
        cell.place_piece(piece)
        removed_piece = cell.remove_piece()
        self.assertEqual(removed_piece, piece)
        self.assertIsNone(cell.get_piece())

    def test_is_occupied(self):
        cell = Cell("white", (0, 0))
        self.assertFalse(cell.is_occupied())
        cell.place_piece("Bishop")
        self.assertTrue(cell.is_occupied())

    def test_place_piece_on_occupied_cell(self):
        cell = Cell("black", (0, 0))
        cell.place_piece("Queen")
        with self.assertRaises(ValueError):
            cell.place_piece("King")

if __name__ == '__main__':
    unittest.main()
