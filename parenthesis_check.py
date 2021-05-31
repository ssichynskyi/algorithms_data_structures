#!usr/bin/python
# -*- coding: utf-8 -*-

from data_structures.stack import Stack

""" Balanced parenthesis check

Problem Statement:
    Given a string of opening and closing parentheses, check whether it’s balanced.
    We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}.
    Assume that the string doesnt contain any other character than these, no spaces words or numbers.
    "Balanced parentheses" require every opening parenthesis to be closed in the reverse order opened.

Example:
    ‘([])’ is balanced but ‘([)]’ is not.

Assume that input string has no spaces.

"""


def is_parentheses_balanced(input_string: str) -> bool:
    """Checks a string for balanced brackets of 3 different kinds: (),{},[].

    Args:
        input_string: a string to be checked

    Returns:
        True if parenthesis are balanced, False in other case

    """
    if input_string is None or not isinstance(input_string, str):
        raise ValueError('Incorrect input parameter! Shall be string')
    brackets_stack = Stack()
    par_dict = {'}': '{', ')': '(', ']': '['}
    for char in input_string:
        if char in par_dict.values():
            brackets_stack.push(char)
        elif char in par_dict.keys():
            last_element = brackets_stack.peek()
            if last_element == par_dict[char]:
                brackets_stack.pop()
            else:
                return False
        else:
            continue
    return brackets_stack.is_empty()
