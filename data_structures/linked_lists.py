#!usr/bin/python
# -*- coding: utf-8 -*-
"""This module implements linked lists and main operations with them"""

from data_structures.stack import Stack


class SinglyListNode:
    """Node for a singly linked list"""
    def __init__(self, value):
        self.next = None
        self.value = value


class DoublyLinkedListNode(SinglyListNode):
    """Node for a doubly linked list"""
    def __init__(self, value):
        super().__init__(value)
        self.prev = None


class IllegalLinkedListOperation(Exception):
    """General exception for illegal operations with linked lists"""
    def __init__(self, *args):
        Exception.__init__(self, *args)


class IllegalListReversalAttempt(IllegalLinkedListOperation):
    """"""
    def __init__(self, message, *args):
        super.__init__(*args)
        self.message = message


class SinglyLinkedList:
    """Implements singly linked list

    ToDo:
        - add cycle length measurement (from the point where fast and slow
        markers met, restart the run. Number of iterations before they meet again
        is the length of the cycle
        - add function to de-cycle the list (make a
        - find the middle of the list (with 2 markers - fast and slo)
    """
    def __init__(self, head=None):
        """
        Args:
            head: head node of the linked list
        """
        self.head = head
        self._tail = None

    @property
    def tail(self):
        """Tail node of the linked list"""
        if not self._tail:
            self.is_linked_list_cycled(self.head)
        return self._tail

    def push(self, value) -> None:
        """Add new node to the linked list and updates the head

        Args:
            value: value of the node that has to be added

        Returns:
            None

        """
        node = SinglyListNode(value)
        node.next = self.head
        self.head = node

    def append(self, value) -> None:
        """Add new node to the tail of the list

        Args:
            value: value of the node that has to be added

        Returns:
            None

        """
        if self.is_linked_list_cycled(self.head):
            raise IllegalLinkedListOperation("Cannot append the node to a cycled list")
        node = SinglyListNode(value)
        if self.head:
            self._tail.next = node
            self._tail = node
        else:
            self.head = node
            self._tail = node

    def is_linked_list_cycled(self, start_node=None) -> bool:
        """Determine if a given singly linked list has cycles

        Note:
            A cycle is when a node's next actually points back to one of
            previous nodes in the list. This is also sometimes known as a
            circularly linked list. It's not possible to perform certain
            operation on such lists. For example: get_length, reverse...

        Idea:
            1. Use two markers: the fast and the slow one.
            2. Slow marker moves one node per iteration.
            3. Fast marker moves two nodes per iteration.
            4. Start running them from head.
            5. If at some iteration nodes are equal, the list is cycled

        Args:
            start_node: node of the list to start from

        Returns:
            True in case given list has cycle.
            In other case False and update of the self._tail

        """
        start_node = self.head if start_node is None else start_node
        marker_slow = start_node
        marker_fast = start_node
        while marker_fast is not None and marker_fast.next is not None:
            marker_fast = marker_fast.next.next
            marker_slow = marker_slow.next
            if marker_fast == marker_slow:
                return True
        return False

    def reverse(self) -> None:
        """Reverses singly linked list

        Returns:
            None, all changes done in linked list

        Raises:
            IllegalListReversalAttempt

        """
        if self.is_linked_list_cycled(self.head):
            raise IllegalListReversalAttempt("Cannot reverse the linked list")
        current_node = self.head
        previous_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node

    def reverse_with_stack(self) -> None:
        """Reverses singly linked list using stack

        Idea:
            Stack reverses the order of the elements.
            So, if we put all nodes to stack and then extract them,
            We will have a reversed linked list

        Note:
            This algorithm is less effective, since it requires additional space
            as well as two iterations - put and pop

        Returns:
            None, all changes done in linked list

        Raises:
            IllegalListReversalAttempt

        """
        if self.is_linked_list_cycled(self.head):
            raise IllegalListReversalAttempt("Cannot reverse the linked list")
        current = self.head
        stack = Stack()
        # put all elements to stack
        while current.next is not None:
            stack.push(current)
            current = current.next
        new_head = current
        # pop all elements from stack and link
        while not stack.is_empty():
            previous = current
            current = stack.pop()
            previous.next = current
        current.next = None
        return new_head

    def values_to_list(self, start_node=None) -> list:
        """Puts all elements of a linked list into list in the same order

        Args:
            start_node: node of a singly linked list to start from

        Returns:
            list of values of linked list nodes

        Raises:
            IllegalListReversalAttempt

        """
        start_node = self.head if start_node is None else start_node
        if self.is_linked_list_cycled(start_node):
            raise IllegalLinkedListOperation("Not possible to return values from cycled list")
        output_list = []
        current = self.head
        while current is not None:
            output_list.append(current.value)
            current = current.next
        return output_list

    def get_length(self, start_node=None) -> int:
        """Determine the length of the list

        Args:
            start_node: node from which the counting shall start

        Returns:
            the length of the list (number of nodes)
        """
        if self.is_linked_list_cycled(start_node):
            raise IllegalLinkedListOperation("Not possible to measure length of a cycled list")

        node = start_node if start_node is not None else self.head
        if self.head is None:
            return 0

        counter = 1
        while node.next:
            node = node.next
            counter += 1
        return counter
