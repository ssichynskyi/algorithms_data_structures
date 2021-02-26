#!usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase

from array_sum_pairs import find_unique_sum_pairs


class TestArraySumPairs(TestCase):
    def setUp(self) -> None:
        pass

    def test_find_unique_sum_pairs_pos_one(self):
        search_array = [1, 9, 8, 2, 3, 7, 6, 4, 5, 5, 13, 14, 11, 13, -1]
        control_number = 10
        # using set, since hashing changes the order of the elements
        verification_set = ((1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (-1, 11))
        pairs = find_unique_sum_pairs(search_array, control_number)
        self.assertTupleElements(pairs, verification_set)

    def test_find_unique_sum_pairs_pos_two(self):
        search_array = [1, 2, 3, 1]
        control_number = 3
        verification_set = ((1, 2),)
        pairs = find_unique_sum_pairs(search_array, control_number)
        self.assertTupleElements(pairs, verification_set)

    def test_find_unique_sum_pairs_pos_three(self):
        search_array = [1, 3, 2, 2]
        control_number = 6
        verification_set = ()
        pairs = find_unique_sum_pairs(search_array, control_number)
        self.assertTupleElements(pairs, verification_set)

    def test_find_unique_sum_pairs_pos_four(self):
        search_array = [0, 0]
        control_number = 0
        verification_set = ((0, 0),)
        pairs = find_unique_sum_pairs(search_array, control_number)
        self.assertTupleElements(pairs, verification_set)

    def test_find_unique_sum_pairs_pos_boundary(self):
        search_array = [1, 3]
        control_number = 4
        verification_set = ((1, 3),)
        pairs = find_unique_sum_pairs(search_array, control_number)
        self.assertTupleElements(pairs, verification_set)

    def test_find_unique_sum_pairs_neg_boundary(self):
        search_array = [0]
        control_number = 0
        with self.assertRaises(ValueError):
            find_unique_sum_pairs(search_array, control_number)

    def test_find_unique_sum_pairs_neg_one(self):
        search_array = ['a', 'b']
        control_number = 'ab'
        with self.assertRaises(TypeError):
            find_unique_sum_pairs(search_array, control_number)

    def tearDown(self) -> None:
        pass

    def assertTupleElements(self, tup1, tup2):
        """ Customized modification for tuple comparison: given tuples are considered equal
        if they contain the same collection of elements, order of elements is ignored

        Args:
            tup1 - first given tuple
            tup2 - second given tuple

        Example:
            ((1,2),(3,4)) is considered as equal to ((3,4),(1,2)) but not to ((1,3),(2,4))

        """
        if not all(isinstance(tup, tuple) for tup in (tup1, tup2)):
            self.fail(msg='Given parameters are not tuples')
        if not len(tup1) == len(tup2):
            self.fail(msg='Given tuples have different length')
        for el1 in tup1:
            if el1 in tup2:
                continue
            else:
                self.fail(msg=f'There is no equivalent of {el1} from first param in {tup2}')
