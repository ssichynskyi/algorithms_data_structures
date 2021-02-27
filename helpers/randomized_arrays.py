#!usr/bin/python
# -*- coding: utf-8 -*-
import random


def get_random_array_of_ints(length: int, lower_bound: int, upper_bound: int) -> [int]:
    """ Creates a list of random integers

    Args:
        length: number of elements in the list
        lower_bound: min value of list element
        upper_bound: max value of list element

    Raises:
        TypeError, ValueError

    Returns:
        list of integers

    """
    if not all((
            isinstance(lower_bound, int),
            isinstance(upper_bound, int),
            isinstance(length, int))):
        raise TypeError('Expected only integer values as params')
    if length <= 0:
        raise ValueError('Array length shall be more, than 0')
    result = []
    for _ in range(length):
        result.append(random.randint(lower_bound, upper_bound))
    return result

