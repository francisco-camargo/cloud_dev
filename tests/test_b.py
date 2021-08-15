import unittest

import sys
if '..' not in sys.path:
    sys.path.append('..')

from src import main

class TestStringMethods(unittest.TestCase):

    def test_simple(self):
        x = 'foo'
        self.assertEqual(main.my_string(), x)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()