#!usr/bin/python
# -*- coding: utf-8 -*-


class IllegalPopAttemptException(Exception):
    """ Exception is raised when pop() is called on an empty stack

    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class Stack:
    """ Custom implementation of a stack data structure """
    def __init__(self, basis=None):
        """ Creates the object of a stack type

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
        """ Returns the last element of the stack without popping it up """
        try:
            return self._items[-1]
        except IndexError:
            return None

    def copy(self):
        """ Returns the stack which is the copy of the current one """
        stack = self.__new__(Stack)
        stack.__init__(self._items)
        return stack


class StackConstTimeMaxEl(Stack):
    """ Stack with the possibility to return the maximum element in a constant time """
    def __init__(self, basis=None):
        super().__init__(basis)
        self._max_value_stack = super().__new__(Stack)
        self._max_value_stack.__init__()
        if basis is not None:
            for element in basis:
                self._update_max_value_stack(element)

    def _update_max_value_stack(self, item) -> None:
        if self._max_value_stack.is_empty():
            self._max_value_stack.push(item)
        else:
            if self._max_value_stack.peek() <= item:
                self._max_value_stack.push(item)

    def push(self, item) -> None:
        self._update_max_value_stack(item)
        super().push(item)

    def pop(self):
        if self._max_value_stack.peek() == self.peek():
            self._max_value_stack.pop()
        return super().pop()

    def get_max(self):
        return self._max_value_stack.peek()
