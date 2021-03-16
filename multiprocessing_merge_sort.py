from multiprocessing import Pool, cpu_count

from algorithms.search_and_sorting import merge_sort_multi_adapted, merge
from helpers.randomized_arrays import get_random_array_of_ints
from helpers.execution_timer import compare_functions
from helpers.sorting_checker import check_array_sorted


def multiprocess_merge_sort(array):
    """Multi-processing version of merge sort

    Note:
        According to test runs on HW 8xCore 3.0 GHz
        noticeable effect starts from list with 100K int elements
        For lists with 200K+ elements coefficient ~ 3.
        Lists with less, than 100K elements perform slower on MP version
        because of time consumed by process spawn

    Args:
        array: list to sort

    Returns:
        sorted list

    """
    cpu_number = cpu_count()
    process_pool = Pool(processes=cpu_number)
    sub_array_size = len(array) // (cpu_number - 1)
    sorting_arrays = [array[i:i + sub_array_size] for i in range(0, len(array), sub_array_size)]
    sorting_arrays = process_pool.map(merge_sort_multi_adapted, sorting_arrays)
    while len(sorting_arrays) > 1:
        sorting_arrays = zip(sorting_arrays[::2], sorting_arrays[1::2])
        sorting_arrays = process_pool.starmap(merge, sorting_arrays)
    return sorting_arrays[0]


if __name__ == '__main__':
    performance_test_array = get_random_array_of_ints(2000000, -100000, 100000)
    report = compare_functions(
        performance_test_array,
        check_array_sorted,
        merge_sort_multi_adapted,
        multiprocess_merge_sort
    )
    print(report)
