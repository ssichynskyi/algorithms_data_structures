#!usr/bin/python
# -*- coding: utf-8 -*-


class Queue:
    """ Custom implementation of queue data structure

    """
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        item = self._items[0]
        self._items = self._items[1:]
        return item

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
