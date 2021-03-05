from unittest import TestCase
from parenthesis_check import is_parentheses_balanced


class Test(TestCase):
    def setUp(self):
        self.test_inputs = {
            '': True,
            '(': False,
            ')': False,
            '([])': True,
            '[(])': False,
            '{}[]()': True,
            '{{[]}()}': True,
            '(122.6 + 74)*{[[A]-a]**{2/d}}': True
        }

    def test_is_parentheses_balanced(self):
        for test_string in self.test_inputs:
            self.assertEqual(is_parentheses_balanced(test_string), self.test_inputs[test_string])

    def test_data_validation(self):
        with self.assertRaises(ValueError):
            is_parentheses_balanced(None)
        with self.assertRaises(ValueError):
            is_parentheses_balanced(3.56)
