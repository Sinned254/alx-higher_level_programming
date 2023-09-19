#!/usr/bin/python3
"""Module contains class ``Base`` base of other
projects, to manage ``id`` attribute in other classes
"""
import json
import csv


class Base:
    """Defination of class Base
    __nb_objects: private class attribute to keep
    track of number of instances created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor initializes class Base
        Args:
            id: optional, if provided it assigns the value of id to the
            public instance attribute id. If id is not provided
            (i.e., it's None), it increments the __nb_objects
            count and assigns the new value to the id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs
        to a file with the appropriate filename.
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(list_dicts)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """that returns a list of dictionaries from a JSON
        string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set using the update method
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances based on the data in a JSON file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_str = file.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**dict_item) for dict_item in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """class method serializes a list of objects to a CSV file.
        Depending on whether it's a Rectangle or Square,
        it writes the appropriate attribute values to the CSV file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """class method deserializes objects from a CSV file.
        It reads the CSV file and creates objects with the
        corresponding attribute values based on whether
        it's a Rectangle or Square.
        """
        filename = cls.__name__ + ".csv"
        objects = []
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                if cls.__name__ == "Rectangle":
                    for row in reader:
                        obj = cls(1, 1)  # Create a dummy instance
                        obj.id = int(row[0])
                        obj.width = int(row[1])
                        obj.height = int(row[2])
                        obj.x = int(row[3])
                        obj.y = int(row[4])
                        objects.append(obj)
                elif cls.__name__ == "Square":
                    for row in reader:
                        obj = cls(1)  # Create a dummy instance
                        obj.id = int(row[0])
                        obj.size = int(row[1])
                        obj.x = int(row[2])
                        obj.y = int(row[3])
                        objects.append(obj)
        except FileNotFoundError:
            pass
        return objects
