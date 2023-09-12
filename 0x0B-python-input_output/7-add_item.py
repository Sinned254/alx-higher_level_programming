#!/usr/bin/python3
"""Module constains funtion to add arguments to python list
"""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_items_to_list_and_save(args, filename):
    """function to add arguments to python list
    Args:
        args: arguments
        filename: filename to save to
    """
    existing_data = load_from_json_file(filename) or []
    existing_data.extend(args)
    save_to_json_file(existing_data, filename)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if arguments:
        filename = "add_item.json"
        add_items_to_list_and_save(arguments, filename)
