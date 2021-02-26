#!usr/bin/python
# -*- coding: utf-8 -*-


class IllegalPopAttemptException(Exception):
    """ Exception is raised when pop() is called on an empty stack

    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class Stack:
    """ Custom implementation of a stack data structure

    """
    def __init__(self, basis=None):
        """ Creates the object of a

        Args:
             basis: a list which shall be the basis for created stack

        """
        if basis:
            if not isinstance(basis, list):
                raise TypeError('Stack could be created only from the list')
            self._items = basis
        else:
            self._items = []

    def pop(self):
        if self.is_empty():
            raise IllegalPopAttemptException('Not possible to pop element from an empty stack')
        return self._items.pop()

    def push(self, item):
        self._items.append(item)

    def is_empty(self):
        return self._items == []

    def peek(self):
        """ Returns the last element of the stack without popping it up

        """
        try:
            return self._items[-1]
        except IndexError:
            return None

    def copy(self):
        """ Returns the stack which is the copy of the current one

        """
        stack = self.__new__(Stack)
        stack.__init__(self._items)
        return stack
