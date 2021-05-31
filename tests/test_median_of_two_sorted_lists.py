from unittest import TestCase
from median_of_two_sorted_lists import find_median_of_two_sorted_lists, median, MyList
from helpers.execution_timer import get_execution_time
from helpers.randomized_arrays import get_random_array_of_ints


class Test(TestCase):
    def setUp(self) -> None:
        self.valid_test_set = (
            (3.5, ([1, 4, 5], [2, 3, 6])),
            (3.0, ([4, 5], [1, 2, 3])),
            (-1, ([3], [-2, -1])),
            (2, ([1, 3], [2])),
            (2.5, ([1, 2], [3, 4])),
            (3.0, ([1, 2, 5], [3, 4])),
            (10.0, ([1, 6, 7, 8, 12, 15, 24, 30, 40, 42], [0, 2, 3, 5, 8, 10, 11, 17, 50])),
            (1.5, ([1], [2])),
            (1.0, ([1], [])),
            (1.5, ([1, 2], [-1, 3]))
        )

    def test_find_median_of_two_sorted_lists(self):
        for expected, test_set in self.valid_test_set:
            self.assertEqual(expected, find_median_of_two_sorted_lists(*test_set))

    def test_find_median_of_two_sorted_lists_random(self):
        test_list_1 = sorted(get_random_array_of_ints(1000, -1000, 1000))
        test_list_2 = sorted(get_random_array_of_ints(1000, -10000, 10000))
        self.assertEqual(
            nlogn_function(test_list_1, test_list_2),
            find_median_of_two_sorted_lists(test_list_1, test_list_2)
        )
        test_list_1 = sorted(get_random_array_of_ints(1000, 0, 1000))
        test_list_2 = sorted(get_random_array_of_ints(1001, -10000, 1000))
        self.assertEqual(
            nlogn_function(test_list_1, test_list_2),
            find_median_of_two_sorted_lists(test_list_1, test_list_2)
        )

    def test_performance(self):
        perf_test_array_1 = sorted(get_random_array_of_ints(100, -10000, 10000))
        perf_test_array_2 = sorted(get_random_array_of_ints(100, -10000, 10000))
        _, time_logn_1 = get_execution_time(
            find_median_of_two_sorted_lists,
            perf_test_array_1, perf_test_array_2
        )
        perf_test_array_1 = sorted(get_random_array_of_ints(1000000, -100000, 100000))
        perf_test_array_2 = sorted(get_random_array_of_ints(1000000, -100000, 100000))
        _, time_logn_2 = get_execution_time(
            find_median_of_two_sorted_lists,
            perf_test_array_1, perf_test_array_2
        )
        # confirm that it is at least < O(n)
        self.assertLess(time_logn_2/time_logn_1, 5000)

    def test_median(self):
        self.assertEqual(1.0, median([1]))
        self.assertEqual(2.0, median([-1, 2, 10]))
        self.assertEqual(3.0, median([-1, 2, 4, 10]))
        with self.assertRaises(ValueError):
            median([])
            median(None)

    def test_my_list(self):
        test_my_list = MyList(-2, 3, [1, 2])
        self.assertEqual(1, test_my_list[0])
        self.assertEqual(2, test_my_list[1])
        self.assertEqual(-2, test_my_list[-1])
        self.assertEqual(-2, test_my_list[-3])
        self.assertEqual(3, test_my_list[2])
        self.assertEqual(3, test_my_list[5])


def nlogn_function(array_one, array_two):
    return median(sorted(array_one + array_two))
