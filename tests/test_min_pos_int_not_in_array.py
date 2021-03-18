from unittest import TestCase

from min_pos_int_not_in_array import solution


class Test(TestCase):
    def setUp(self):
        self.test_set = (
            (1, [-1, -2]),
            (1, []),
            (5, [0, 1, 2, 3, 4]),
            (3, [1, 2, 4])
        )

    def test_find_min_pos_int(self):
        for expected_result, input_array in self.test_set:
            self.assertEqual(expected_result, solution(input_array))
