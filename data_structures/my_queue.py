#!usr/bin/python
# -*- coding: utf-8 -*-


class IllegalDequeueAttemptException(Exception):
    """ Exception is raised when pop() is called on an empty queue """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class DataIntegrityException(Exception):
    """ Exception is raised when there's misalignment between data """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class Queue:
    """ Custom implementation of queue data structure """
    def __init__(self, basis=None):
        """ Creates the object of a queue type
        Args:
             basis: a list which shall be the basis for created queue
        """
        if basis is None:
            self._items = []
        else:
            self._items = basis

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if len(self._items) == 0:
            raise IllegalDequeueAttemptException('Not possible to dequeue from an empty queue')
        item = self._items[0]
        self._items = self._items[1:]
        return item

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)


class ErasableQueue(Queue):
    """ Basic queue with the possibility to erase all data """
    def __init__(self, basis=None):
        super().__init__(basis)

    def erase(self):
        self._items = []


class OrderedErasableQueue(ErasableQueue):
    """ Erasable queue with sorting data. It will store only values that
        smaller than preceding element.

    """
    def __init__(self, basis=None):
        super().__init__(basis)

    def enqueue(self, item):
        """ Enqueues the item and erases all preceding elements smaller than self """
        for i in range(len(self._items) - 1, -1, -1):
            if self._items[i] >= item:
                break
        else:
            self._items = [item]
            return
        self._items = self._items[:i+1] + [item]
        return


class QueueConstTimeMaxEl(Queue):
    """ Queue with the possibility to return the maximum element in a constant time

        Explanation:
            Class instance stores the current maximum value as a variable.
            Apart from that it also stores all maximal elements after this maximum
            in a queue. This queue has a descending order because it makes no sense to
            store elements with lower value that are preceding those with high value.

    """
    def __init__(self, basis=None):
        super().__init__(basis=basis)
        self._max_value = None
        self._beyond_max_value_queue = super().__new__(OrderedErasableQueue)
        self._beyond_max_value_queue.__init__()
        if basis is not None:
            for element in basis:
                self._update_max_value_holders_on_enqueue(element)

    def _update_max_value_holders_on_enqueue(self, item):
        if self._max_value is None:
            self._max_value = item
            return
        if item > self._max_value:
            # if the latest element has value more than current max, it replaces it
            # it also makes no sense to keep values in queue anymore
            self._beyond_max_value_queue.erase()
            self._max_value = item
        else:
            self._beyond_max_value_queue.enqueue(item)

    def _update_max_value_holders_on_dequeue(self):
        if self._max_value is None:
            if self._items or self._beyond_max_value_queue.size():
                raise DataIntegrityException(
                    'Data integrity problem! Maximum value is empty while one of queues is full!'
                )
            return
        if self._items[0] == self._max_value:
            if self._beyond_max_value_queue.size() > 0:
                self._max_value = self._beyond_max_value_queue.dequeue()
            else:
                self._max_value = None

    def enqueue(self, item):
        self._update_max_value_holders_on_enqueue(item)
        super().enqueue(item)

    def dequeue(self):
        self._update_max_value_holders_on_dequeue()
        return super().dequeue()

    def get_max(self):
        return self._max_value
