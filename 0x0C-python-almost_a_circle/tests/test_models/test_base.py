#!/usr/bin/python3
"""test class for base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """defiantion"""
    def test_base_constructor_with_id(self):
        """check with id"""
        base_obj = Base(1)
        self.assertEqual(base_obj.id, 1)

    def test_base_constructor_without_id(self):
        """Check without id"""
        base_obj = Base()
        self.assertTrue(hasattr(base_obj, 'id')

     def test_base_to_json_string(self):
        list_dicts = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(json_str, '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]')

    def test_base_from_json_string(self):
        json_str = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        list_dicts = Base.from_json_string(json_str)
        self.assertEqual(list_dicts, [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}])

    def test_base_create(self):
        dict_item = {"id": 1, "width": 5, "height": 10}
        rect_obj = Rectangle.create(**dict_item)
        self.assertIsInstance(rect_obj, Rectangle)
        self.assertEqual(rect_obj.id, 1)
        self.assertEqual(rect_obj.width, 5)
        self.assertEqual(rect_obj.height, 10)

    def test_base_load_from_file(self):
        json_str = '[{"id": 1, "size": 5}, {"id": 2, "size": 10}]'
        with open('Square.json', mode='w', encoding='utf-8') as file:
            file.write(json_str)

        square_list = Square.load_from_file()
        self.assertIsInstance(square_list, list)
        self.assertEqual(len(square_list), 2)
        self.assertIsInstance(square_list[0], Square)
        self.assertEqual(square_list[0].id, 1)
        self.assertEqual(square_list[0].size, 5)
        self.assertIsInstance(square_list[1], Square)
        self.assertEqual(square_list[1].id, 2)
        self.assertEqual(square_list[1].size, 10)

if __name__ == '__main__':
    unittest.main()
