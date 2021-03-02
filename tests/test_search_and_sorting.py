from unittest import TestCase

from helpers.sorting_checker import check_array_sorted
from helpers.execution_timer import compare_functions
from helpers.randomized_arrays import get_random_array_of_ints
from search_and_sorting import (
    bubble_sort,
    selection_sort,
    quick_sort,
    insertion_sort,
    shell_sort,
    merge_sort
)


# result = compare_functions(
#     get_random_array_of_ints(int(1e+5), int(-1e+6), int(1e+6)),
#     check_array_sorted,
#     shell_sort, merge_sort, quick_sort
# )
# for key in result:
#     print(f'{key}: Status: {"Fail" if result[key]["Verification"] == False else "OK"} Time: {result[key]["time ms"]}')

class Test(TestCase):
    def setUp(self) -> None:
        self.random_test_array = get_random_array_of_ints(100, -100, 100)
        self.duplicates_array = [1, 1, 1, 1]
        self.duplicates_of_two_types = [-1, 0, -1, 0, -1]
        self.empty_array = []
        self.test_set = (
            self.random_test_array,
            self.duplicates_array,
            self.duplicates_of_two_types,
            self.empty_array
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

    def generic_test(self, func):
        for array in self.test_set:
            test_array = array.copy()
            func(test_array)
            self.assertTrue(check_array_sorted(test_array))
