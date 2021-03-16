import concurrent.futures as concurrent_futures
from threading import Lock

from algorithms.search_and_sorting import (
    heap_sort,
    counting_sort,
    merge_sort,
    quick_sort,
    shell_sort,
    radix_sort
)
from helpers.randomized_arrays import get_random_array_of_ints


def compete():
    sorting_functions = (
        quick_sort,
        shell_sort,
        merge_sort,
        counting_sort,
        radix_sort,
        heap_sort
    )

    def run(func, args):
        nonlocal number
        func(args)
        with lock:
            print(f'Sorting function {func.__name__} comes on place {number}')
            number += 1

    number = 1
    lock = Lock()
    performance_test_array = get_random_array_of_ints(100000, -10000, 10000)
    test_array_pool = [performance_test_array.copy() for _ in range(len(sorting_functions))]
    with concurrent_futures.ThreadPoolExecutor() as executor:
        sorted_list_futures = [
            executor.submit(run, sorting_functions[i], test_array_pool[i]) for i in range(len(sorting_functions))
        ]


if __name__ == '__main__':
    compete()
