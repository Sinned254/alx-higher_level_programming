#!/usr/bin/python3
"""test class for ``rectangle`` class
"""
import unittest
from models.base import Base


class TestRectangle(unittest.TestCase):
    def test_rectangle_constructor_with_id(self):
        rect_obj = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(rect_obj.id, 10)

    def test_rectangle_constructor_without_id(self):
        rect_obj = Rectangle(4, 5, 1, 2)
        self.assertTrue(hasattr(rect_obj, 'id'))

    def test_rectangle_attributes(self):
        rect_obj = Rectangle(4, 5, 1, 2)
        self.assertEqual(rect_obj.width, 4)
        self.assertEqual(rect_obj.height, 5)
        self.assertEqual(rect_obj.x, 1)
        self.assertEqual(rect_obj.y, 2)

    def test_rectangle_invalid_width(self):
        with self.assertRaises(ValueError):
            rect_obj = Rectangle(0, 5, 1, 2)

    def test_rectangle_invalid_height(self):
        with self.assertRaises(ValueError):
            rect_obj = Rectangle(4, -5, 1, 2)

    def test_rectangle_invalid_x(self):
        with self.assertRaises(ValueError):
            rect_obj = Rectangle(4, 5, -1, 2)

    def test_rectangle_invalid_y(self):
        with self.assertRaises(ValueError):
            rect_obj = Rectangle(4, 5, 1, -2)
    def test_rectangle_area(self):
        rect_obj = Rectangle(4, 5)
        self.assertEqual(rect_obj.area(), 20)

    def test_rectangle_display(self):
        rect_obj = Rectangle(3, 2, 2, 1)
        expected_output = "  ###\n  ###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect_obj.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_rectangle_update_args(self):
        rect_obj = Rectangle(4, 5, 1, 2)
        rect_obj.update(10, 6, 7, 3, 4)
        self.assertEqual(rect_obj.id, 10)
        self.assertEqual(rect_obj.width, 6)
        self.assertEqual(rect_obj.height, 7)
        self.assertEqual(rect_obj.x, 3)
        self.assertEqual(rect_obj.y, 4)

    def test_rectangle_update_kwargs(self):
        rect_obj = Rectangle(4, 5, 1, 2)
        rect_obj.update(id=10, width=6, height=7, x=3, y=4)
        self.assertEqual(rect_obj.id, 10)
        self.assertEqual(rect_obj.width, 6)
        self.assertEqual(rect_obj.height, 7)
        self.assertEqual(rect_obj.x, 3)
        self.assertEqual(rect_obj.y, 4)

    def test_rectangle_to_dictionary(self):
        rect_obj = Rectangle(5, 4, 2, 3)
        rect_dict = rect_obj.to_dictionary()
        expected_dict = {'id': 1, 'width': 5, 'height': 4, 'x': 2, 'y': 3}
        self.assertEqual(rect_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
