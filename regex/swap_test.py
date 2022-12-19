#!/usr/bin/env python3

from swap import name_swap
import unittest

class TestSwapName(unittest.TestCase):
    def test_basic(self):
        testcase = "Challa Puneeth Reddy"
        expected = "Puneeth R. Challa"
        self.assertEqual(name_swap(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(name_swap(testcase), expected)
    
    def test_two_name(self):
        testcase = "Challa Puneeth"
        expected = "Puneeth Challa"
        self.assertEqual(name_swap(testcase), expected)
    
    def test_one_name(self):
        testcase = "Puneeth"
        expected = "Puneeth"
        self.assertEqual(name_swap(testcase), expected)

if __name__ == '__main__':
    unittest.main()