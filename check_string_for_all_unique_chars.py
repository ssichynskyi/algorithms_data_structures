#!usr/bin/python
# -*- coding: utf-8 -*-

"""
UNIQUE CHARACTERS IN STRING

Problem
Given a string,determine if it is comprised of only unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'abcdde' contains duplicate characters and should return false.

"""


def is_composed_of_unique_characters(input_string: str) -> bool:
    """ Determine if all elements in string are unique (i.e. present only 1 time)
    Args:
        input_string: string to examine

    Return:
        True, if string is composed from only unique elements. Otherwise - False

    """
    return len(set(input_string)) == len(input_string)
