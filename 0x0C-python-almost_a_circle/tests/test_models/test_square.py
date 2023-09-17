#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_constructor_with_id(self):
        square_obj = Square(5, 2, 3, 1)
        self.assertEqual(square_obj.id, 1)

    def test_square_constructor_without_id(self):
        square_obj = Square(5, 2, 3)
        self.assertTrue(hasattr(square_obj, 'id'))

    def test_square_attributes(self):
        square_obj = Square(5, 2, 3)
        self.assertEqual(square_obj.size, 5)
        self.assertEqual(square_obj.width, 5)
        self.assertEqual(square_obj.height, 5)
        self.assertEqual(square_obj.x, 2)
        self.assertEqual(square_obj.y, 3)

    def test_square_invalid_size(self):
        with self.assertRaises(ValueError):
            square_obj = Square(-5, 2, 3)

    def test_square_invalid_x(self):
        with self.assertRaises(ValueError):
            square_obj = Square(5, -2, 3)

    def test_square_invalid_y(self):
        with self.assertRaises(ValueError):
            square_obj = Square(5, 2, -3)

    def test_square_area(self):
        square_obj = Square(5)
        self.assertEqual(square_obj.area(), 25)

    def test_square_display(self):
        square_obj = Square(3, 2, 1)
        expected_output = "  ###\n  ###\n  ###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square_obj.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_square_update_args(self):
        square_obj = Square(5, 2, 3)
        square_obj.update(10, 6, 4, 1)
        self.assertEqual(square_obj.id, 10)
        self.assertEqual(square_obj.size, 6)
        self.assertEqual(square_obj.x, 4)
        self.assertEqual(square_obj.y, 1)

    def test_square_update_kwargs(self):
        square_obj = Square(5, 2, 3)
        square_obj.update(id=10, size=6, x=4, y=1)
        self.assertEqual(square_obj.id, 10)
        self.assertEqual(square_obj.size, 6)
        self.assertEqual(square_obj.x, 4)
        self.assertEqual(square_obj.y, 1)

    def test_square_to_dictionary(self):
        square_obj = Square(5, 2, 3)
        square_dict = square_obj.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
