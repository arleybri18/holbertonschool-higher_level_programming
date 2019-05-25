#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer(), None)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_strings_in_list(self):
        with self.assertRaises(TypeError) as msg:
            max_integer([1, "a", 2])
            self.assertEqual(msg.message, "unorderable types: str() > int()")

    def test_tuple_instead_list(self):
        self.assertEqual(max_integer((1, 2)), 2)

