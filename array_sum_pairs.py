#!usr/bin/python
# -*- coding: utf-8 -*-
import argparse

from helpers.execution_timer import measure
from typing import Tuple

""" ARRAY PAIR SUM

Problem:
    Given an integer search_array, output all the unique pairs that sum up to a specific value k.

Example:
    Input: pair_sum([1,3,2,2], 4)
    Output:
        (1,3)
        (2,2)
"""


def solution(search_array: [int], control_number: int) -> None:
    """ Executes the program that solves the given problem, measures time
    and organizes output to a console

    Args:
        search_array: array of integers where the search shall happen
        control_number: number which is all digits shall be check against

    """
    print('Given inputs: \"{0}\" and \"{1}\"'.format(search_array, control_number))
    try:
        pairs = measure(find_unique_sum_pairs, search_array, control_number)
    except (ValueError, TypeError) as e:
        print(f'Exception during the execution: \n {str(e)}')

    if len(pairs) == 0:
        print(f'No unique pairs which sum is equal to {control_number} found in a given array')
    else:
        print(f'Unique pairs which sum is equal to {control_number} in a given array are:')
        for pair in pairs:
            print(pair)
    return


def find_unique_sum_pairs(search_array: [int], control_number: int) -> Tuple[Tuple[int, int]]:
    """ Discovers all unique pairs in search_array which sum is equal to a control_number

    Args:
        search_array: array of integers where the search shall happen
        control_number: number which is all digits shall be check against

    Returns:
        unique pairs in form of tuples (min, max)

    """
    if len(search_array) < 2:
        raise ValueError('Array shall have at least 2 elements')
    # EXPLANATION TO A SOLUTION
    # in general, algorithm shall collect all unique elements and check if there's a missing addendum
    # However, removing the element who have found a pair seen.pop(element) -
    # is not necessary as we're looking for only unique pairs, not all pairs

    # temp data set to hold elements that have been already seen
    seen = set()
    # pairs set of tuples - pair of values (min, max)
    pairs = set()

    for element in search_array:
        missing_addendum = control_number - element
        if missing_addendum in seen:
            pairs.add((min(missing_addendum, element), max(missing_addendum, element)))
        else:
            seen.add(element)
    return tuple(pairs)


if __name__ == "__main__":
    command_line_arg_parser = argparse.ArgumentParser()
    command_line_arg_parser.add_argument(
        'search_array',
        help='''provide an array of integers to discover all the unique pairs that are equal to predefined integer
        format: "[1,2,3]"''',
        type=str,
    )
    command_line_arg_parser.add_argument(
        'control_number',
        help='provide a predefined integer to discover all the unique pairs in a given array which sum it is equal to',
        type=int
    )
    args = command_line_arg_parser.parse_args()
    search_array = [int(el) for el in args.search_array.replace('[', '').replace(']', '').split(',')]
    solution(search_array, args.control_number)
