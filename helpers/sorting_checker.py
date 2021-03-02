#!usr/bin/python
# -*- coding: utf-8 -*-


def check_array_sorted(array) -> bool:
    """Checks if given array is sorted

    Args:
        array: list that shall be checked

    Returns:
        True if array is sorted, False in other case

    """
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True
