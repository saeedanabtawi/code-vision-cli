import unittest
from core.loader import load, filter, helper


class MyTestCase(unittest.TestCase):
    def test_remove_spaces_normal_string(self):
        self.assertEqual(filter.remove_spaces("Hello World") == "HelloWorld")

if __name__ == '__main__':
    unittest.main()
