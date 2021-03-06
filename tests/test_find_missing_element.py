from random import shuffle
from unittest import TestCase

from find_missing_element import (
    find_missing_element_with_summing,
    find_missing_element_with_xor,
    find_missing_element_with_sort,
    find_missing_element_with_hash
)


class Test(TestCase):
    def setUp(self):
        self.test_set_pos_ints = {
            1: ([1], []),
            8: ([1, 3, 5, 7, 9, 0, 2, 4, 6, 8], [2, 9, 6, 3, 4, 5, 1, 0, 7]),
            0: ([1, 3, 5, 7, 9, 0, 2, 4, 6, 8], [2, 9, 6, 3, 4, 5, 1, 7, 8])
        }
        self.test_set_neg_ints = {
            8: ([1, -3, 5, -7, 9, 0, -2, 4, 6, 8], [-2, 9, 6, -3, 4, 5, 1, 0, -7]),
            0: ([1, -3, 5, -7, 9, 0, -2, 4, 6, 8], [-2, 9, 6, -3, 4, 5, 1, -7, 8]),
            -3: ([1, -3, 5, -7, 9, 0, -2, 4, 6, 8], [-2, 9, 6, 4, 5, 1, -7, 8, 0])
        }
        self.test_set_floats = {
            1.1: ([1.1, 2.5], [2.5]),
            0.0: ([-1.6, 0.0, 5.4], [-1.6, 5.4]),
            5.4: ([-1.6, 0.0, 5.4], [0.0, -1.6])
        }
        self.test_set_chars = {
            'z': (['a', 'z', '0'], ['0', 'a'])
        }
        # keys below have no value, implemented for data conformance
        self.test_raises_value_error = {
           'x': ([], []),
           'y': ([0], [0])
        }

    def test_find_missing_element_with_summing(self):
        self.generic_test(self.test_set_pos_ints, find_missing_element_with_summing)
        self.generic_test(self.test_set_neg_ints, find_missing_element_with_summing)
        self.generic_test(self.test_set_floats, find_missing_element_with_summing)
        self.generic_negative_test(self.test_raises_value_error, find_missing_element_with_summing)

    def test_find_missing_element_with_sort(self):
        self.generic_test(self.test_set_pos_ints, find_missing_element_with_sort)
        self.generic_test(self.test_set_neg_ints, find_missing_element_with_sort)
        self.generic_test(self.test_set_floats, find_missing_element_with_sort)
        self.generic_test(self.test_set_chars, find_missing_element_with_sort)

    def test_find_missing_element_with_hash(self):
        self.generic_test(self.test_set_pos_ints, find_missing_element_with_hash)
        self.generic_test(self.test_set_neg_ints, find_missing_element_with_hash)
        self.generic_test(self.test_set_floats, find_missing_element_with_hash)
        self.generic_test(self.test_set_chars, find_missing_element_with_hash)
        self.generic_negative_test(self.test_raises_value_error, find_missing_element_with_hash)

    def test_find_missing_element_with_xor(self):
        self.generic_test(self.test_set_pos_ints, find_missing_element_with_xor)
        self.generic_test(self.test_set_neg_ints, find_missing_element_with_xor)
        self.generic_negative_test(self.test_raises_value_error, find_missing_element_with_xor)

    def generic_test(self, test_set: dict, func) -> None:
        for answer in test_set.keys():
            self.assertEqual(answer, func(*test_set[answer]))

    def generic_negative_test(self, test_set: dict, func) -> None:
        for answer in test_set.keys():
            with self.assertRaises(ValueError):
                func(*test_set[answer])
