#!usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict


"""FIND THE MISSING ELEMENT

Problem:
    Consider an array of non-negative integers.
    A second array is formed by shuffling the elements of the first array and deleting a random element.
    Given these two arrays, find which element is missing in the second array.

Example:
    Input:
    finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]) #number 5 was removed after shuffling
    
    Output:
    5 is the missing number

"""


def find_missing_element_with_summing(initial_list: list, shuffled_list: list):
    """Sum up all elements from the first and second list.

    Idea:
        1. Sum up all elements from the first and second list.
        2. Subtract sum1 from sum2. The remainder is a searched number
        3. If remainder is 0 and len(

    Notes:
        This solution may not be suitable for other programming languages.
        But in Python int has an unlimited length.

        Advantages:
            - Fast, time performance is O(N), O(1) space performance
            - Can work with any numeric data, e.g. float
        Drawbacks:
            - non-universal, cannot be applied for similar tasks with little deviations.
            e.g. when arbitrary amount of elements is removed or lists are completely different.

    Args:
        initial_list: model list
        shuffled_list: list which is a shuffled initial_list with all but one elements present

    Returns:
        An element of the initial list which is absent in a shuffled one

    Raises:
        ValueError

    """
    _check_input_data(initial_list, shuffled_list)
    return sum(initial_list) - sum(shuffled_list)


def find_missing_element_with_sort(initial_list, shuffled_list):
    """Find missing element using array sort.

    Idea:
        sort given list and find first inconsistency

    Notes:
        Advantages:
            - Can work with any consistent comparable data, e.g. float, char, etc.
            - universal, can be applied for similar tasks with little deviations.
            e.g. when arbitrary amount of elements is removed or lists are completely different.

        Drawbacks:
            - Poor time performance (depends on sorting function used)

    Args:
        initial_list: model list
        shuffled_list: list which is a shuffled initial_list with all but one elements present

    Returns:
        An element of the initial list which is absent in a shuffled one

    """
    initial_list.sort()
    shuffled_list.sort()
    for i in range(len(initial_list) - 1):
        if shuffled_list[i] != initial_list[i]:
            return initial_list[i]
    return initial_list[-1]


def find_missing_element_with_hash(initial_list, shuffled_list):
    """Find missing element using hash table

    Idea:
        register all occurrences from initial list in a hash table,
        where key = element and value = number of occurrences

    Notes:
        defaultdict is used instead of dict in order to optimize the number
        of try/except blocks. defaultdict doesnt raise KeyError.

        Advantages:
            - Can work with any consistent data (e.g. float, char, etc.)
            even when it's not comparable. Must be hashable.
            - universal, can be applied for similar tasks with little deviations.
            e.g. when arbitrary amount of elements is removed or lists are completely different.
            - Fast, time performance is O(N)

        Drawbacks:
            - Space/memory performance is O(N)

    Args:
        initial_list: model list
        shuffled_list: list which is a shuffled initial_list with all but one elements present

    Returns:
        An element of the initial list which is absent in a shuffled one

    Raises:
        ValueError

    """
    hash_table = defaultdict(int)
    for element in shuffled_list:
        hash_table[element] += 1

    for element in initial_list:
        if hash_table[element] == 0:
            return element
        hash_table[element] -= 1

    raise ValueError("""Was not possible to find missing element.
    Check if input arrays satisfy the criterion""")


def find_missing_element_with_xor(initial_list, shuffled_list):
    """Find missing element using bitwise XOR

    Idea:
        XOR acts similar to summing up but ignoring the overflow of higher bit.
        Also bitwise XOR for equal elements = 0,
        therefore only bits of the missing element at the end will be in place

    Notes:
        Advantages:
            - Fast, time performance is O(N)
            - Space/memory performance is O(1)

        Drawbacks:
            - can work only with int/bool data

    Args:
        initial_list: model list
        shuffled_list: list which is a shuffled initial_list with all but one elements present

    Returns:
        An element of the initial list which is absent in a shuffled one

    """
    _check_input_data(initial_list, shuffled_list)
    result = type(initial_list[0])()
    for element in initial_list + shuffled_list:
        result = result ^ element
    return result


def _check_input_data(initial_list: list, shuffled_list: list) -> None:
    """Checks if a given data is compliant with the requirements"""
    if len(initial_list) - len(shuffled_list) != 1:
        raise ValueError('Second array shall be the shuffled first array with only one element removed!')
