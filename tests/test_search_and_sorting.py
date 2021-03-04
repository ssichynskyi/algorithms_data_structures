from unittest import TestCase

from helpers.execution_timer import compare_functions
from helpers.randomized_arrays import get_random_array_of_ints
from helpers.sorting_checker import check_array_sorted
from search_and_sorting import (
    bubble_sort,
    selection_sort,
    quick_sort,
    insertion_sort,
    shell_sort,
    merge_sort,
    counting_sort,
    radix_sort
)


class Test(TestCase):
    def setUp(self) -> None:
        self.random_test_array = get_random_array_of_ints(100, -100, 100)
        self.duplicates_array = [1, 1, 1, 1]
        self.duplicates_of_two_types = [-1, 0, -1, 0, -1]
        self.empty_array = []
        self.test_set = (
            self.duplicates_array,
            self.duplicates_of_two_types,
            self.empty_array,
            self.random_test_array
        )
        self.sorting_functions = (
            quick_sort,
            shell_sort,
            merge_sort,
            counting_sort,
            radix_sort
        )

    def test_bubble_sort(self):
        self.generic_test(bubble_sort)

    def test_selection_sort(self):
        self.generic_test(selection_sort)

    def test_insertion_sort(self):
        self.generic_test(insertion_sort)

    def test_shell_sort(self):
        self.generic_test(shell_sort)

    def test_merge_sort(self):
        self.generic_test(merge_sort)

    def test_quick_sort(self):
        self.generic_test(quick_sort)

    def test_counting_sort(self):
        self.generic_test(counting_sort)

    def test_radix_sort(self):
        self.generic_test(radix_sort)

    def generic_test(self, func):
        for array in self.test_set:
            test_array = array.copy()
            func(test_array)
            self.assertTrue(check_array_sorted(test_array))

    def test_performance(self):
        performance_test_array = get_random_array_of_ints(10000, -10000, 10000)
        results = compare_functions(performance_test_array, check_array_sorted, *self.sorting_functions)
        for func_name in results:
            print(f'{func_name}: {results[func_name]}')
