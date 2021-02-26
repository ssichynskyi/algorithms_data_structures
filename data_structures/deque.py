#!usr/bin/python
# -*- coding: utf-8 -*-


class Deque:
    """ Custom implementation of the double-ended queue """
    def __init__(self):
        self._items = []

    def add_front(self, item):
        self._items.insert(0, item)

    def add_rear(self, item):
        self._items.append(item)

    def pop_front(self):
        item = self._items[0]
        self._items = self._items[1:]
        return item

    def pop_rear(self):
        return self._items.pop()

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)
