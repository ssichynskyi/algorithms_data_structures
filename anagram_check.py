#!usr/bin/python
# -*- coding: utf-8 -*-
import argparse

from helpers.execution_timer import measure
from typing import Tuple

""" ANAGRAM CHECK
Problem:
    Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using
    the exact same letters (so you can just rearrange the letters to get a different phrase or word).

Example:
    "public relations" is an anagram of "crap built on lies"
    "clint eastwood" is an anagram of "old west action"
    
Usage:
    python anagram_check.py <first string> <second string> <number of solution to run>
    e.g.:
    python anagram_check.py "baba" "abba" 1
"""


def solution(first: str, second: str, solution_number: int) -> None:
    """ Runs the program that determines if two given strings are anagrams
    and measures the execution time using one of 3 solutions

    Args:
        first - first string
        second - second string
        solution_number - [1..3] selector of the problem solution

    Returns:
        prints the result and execution time into console

    """
    solution_switch = {
        1: is_anagram_one,
        2: is_anagram_two,
        3: is_anagram_three
    }
    print(rf'Given strings: "{first}" and "{second}"')
    # prepare strings
    try:
        first, second = _prepare_strings(first, second)
    except TypeError as e:
        print(str(e))
    except ValueError as e:
        print(str(e))
    result = measure(solution_switch[solution_number], first, second)
    if result:
        print('These solutions are anagrams!')
    else:
        print('These solutions are NOT anagrams')
    return


def _prepare_strings(*strings) -> Tuple[str]:
    """ Does sanitation of the given strings as parameters:
    - removing spaces
    - change all upper-case to lower-case

    Args:
        strings - a tuple of strings that has to be pre-checked

    Returns:
        A tuple of strings after all sanitation is done

    Raises:
        TypeError if not strings or has zero length

    """
    result = []
    for string in strings:
        if type(string) != str:
            raise TypeError('One of the given parameters is not of a string-type')
        string = string.replace(' ', '').lower()
        if len(string) == 0:
            raise ValueError('String shall contain at least one non-space symbol')
        result.append(string)
    return tuple(result)


def _size_pre_check(*strings) -> bool:
    """ Checks if given strings have the same number of elements

    Args:
        strings - a tuple of strings that has to be pre-checked

    Returns:
        True if all strings passed as params have the same number of elements
        False in other case

    Raises:
        ValueError if arguments is not a list of strings

    """
    length = None
    for string in strings:
        if not isinstance(string, str):
            raise ValueError(f'Expected strings as arguments! {type(string)} is given')
        if length is None:
            length = len(string)
        else:
            if len(string) != length:
                return False
    return True


def is_anagram_one(first: str, second: str) -> bool:
    """ First variant of solution if two strings are anagrams.
    For every symbol in first string find and remove it's occurrence in the second.

    Args:
        first - first given string
        second - second given string

    Returns:
        True if all strings passed as params have the same number of elements
        False in other case

    """
    if not _size_pre_check(first, second):
        return False
    for char in first:
        try:
            i = second.index(char)
        except ValueError:
            return False
        second = second[:i] + second[i+1:]
    return True


def is_anagram_two(first: str, second: str) -> bool:
    """ Second variant of solution if two strings are anagrams.
    Sort and compare lists of symbols

    Args:
        first - first given string
        second - second given string

    Returns:
        True if all strings passed as params have the same number of elements
        False in other case

    """
    if not _size_pre_check(first, second):
        return False
    a = list(first)
    b = list(second)
    if a.sort() == b.sort():
        return True
    return False


def is_anagram_three(first: str, second: str) -> bool:
    """ Third variant of solution if two strings are anagrams.
    Counting symbols while hashing them

    Args:
        first - first given string
        second - second given string

    Returns:
        True if all strings passed as params have the same number of elements
        False in other case

    """
    if not _size_pre_check(first, second):
        return False
    letter_register = {}
    for letter in first:
        if letter in letter_register:
            letter_register[letter] += 1
        else:
            letter_register[letter] = 1
    for letter in second:
        if letter in letter_register:
            letter_register[letter] -= 1
        else:
            return False
    for letter in letter_register:
        if letter_register[letter] != 0:
            return False
    return True


if __name__ == "__main__":
    command_line_arg_parser = argparse.ArgumentParser()
    command_line_arg_parser.add_argument(
        'first_string',
        help='give 2 strings to check if they are an anagram one of another',
        type=str
    )
    command_line_arg_parser.add_argument(
        'second_string',
        help='give 2 strings to check if they are an anagram one of another',
        type=str
    )
    command_line_arg_parser.add_argument(
        'solution_number',
        help='give a number to check the exact implementation or leave empty. Debug only',
        type=int,
        nargs='?',
        default=1,
    )
    args = command_line_arg_parser.parse_args()
    solution(args.first_string, args.second_string, args.solution_number)
