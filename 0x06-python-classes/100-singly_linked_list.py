#!/usr/bin/python3
"""Module contains the Node and ''singlyLinkedlist" classes"""


class Node:
    """Node Class"""
    def __init__(self, data):
        """method initialize class Node"""
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Class SinglyLinkedList"""

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None and current.next.data < value:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def __str__(self):
        if self.head is None:
            return "The list is empty."

        current = self.head
        result = ""
        while current:
            result += str(current.data) + "\n"
            current = current.next
        return result
