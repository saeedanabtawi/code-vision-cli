import unittest
from core.loader import load, filter, helper

class MockCode:
    def __init__(self, text):
        self.text = text

class MyTestCase(unittest.TestCase):
    def test_remove_spaces_normal_string(self):
        code = MockCode("Hello World")
        self.assertEqual(filter.remove_spaces(code), "HelloWorld")

    def test_remove_spaces_no_spaces(self):
        code = MockCode("HelloWorld")
        self.assertEqual(filter.remove_spaces(code), "HelloWorld")

    def test_remove_spaces_only_spaces(self):
        code = MockCode("     ")
        self.assertEqual(filter.remove_spaces(code), "")

    def test_remove_spaces_special_characters(self):
        code = MockCode("Hello @ World!")
        self.assertEqual(filter.remove_spaces(code), "Hello@World!")

    def test_remove_spaces_empty_string(self):
        code = MockCode("")
        self.assertEqual(filter.remove_spaces(code), "")



if __name__ == '__main__':
    unittest.main()
