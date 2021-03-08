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
    """
    def __init__(self, head=None):
        """
        Args:
            head: head node of the linked list
        """
        if head and not isinstance(head, SinglyListNode):
            raise TypeError(f'Head must be of type SinglyListNode. Given: {type(head)}')
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

    def get_node_by_position(self, position: int) -> [SinglyListNode, None]:
        """Get the node which is positioned "position" times next to head node

        Args:
            position: number of nodes from head to the requested one. 0 is head.

        Returns:
            Node or None

        """
        if self.is_linked_list_cycled(self.head):
            raise IllegalLinkedListOperation('Cannot get node by its position for a cycled list')
        if not isinstance(position, int) or position < 0:
            raise ValueError('Position index must be non-negative integer')
        current_node = self.head
        counter = 0
        while counter < position:
            if current_node.next is None:
                return None
            current_node = current_node.next
            counter += 1
        return current_node

    def get_node_by_position_reversed(self, position: int) -> [SinglyListNode, None]:
        """Get the node which is positioned "position" times from the tail node

        Args:
            position: number of nodes from tail to the requested one. 0 is tail.

        Returns:
            Node or None

        """
        if self.is_linked_list_cycled(self.head):
            raise IllegalLinkedListOperation('Cannot get node by its position for a cycled list')
        if not isinstance(position, int) or position < 0:
            raise ValueError('Position index must be non-negative integer')
        trailing_pointer = self.head
        leading_pointer = self.head
        for _ in range(position):
            if leading_pointer.next is None:
                return None
            leading_pointer = leading_pointer.next
        while leading_pointer.next is not None:
            trailing_pointer = trailing_pointer.next
            leading_pointer = leading_pointer.next
        return trailing_pointer

    def insert_on_position(self, value, position: int) -> None:
        """Creates a node with given value and puts it "position" times to the right of head

        Args:
            value: the value of the node to be inserted
            position: distance from the head node

        Returns:
            None

        """
        node = SinglyListNode(value)
        self.insert_node_on_position(node, position)

    def insert_node_on_position(self, node: SinglyListNode, position: int) -> None:
        """Puts a given node in "position" times to the right of head node

        Args:
            node: the value of the node to be inserted
            position: distance from the head node

        Returns:
            None

        """
        if position == 0:
            node.next = self.head
            self.head = node
        else:
            preceding_node = self.get_node_by_position(position - 1)
            node.next = preceding_node.next
            preceding_node.next = node

    @staticmethod
    def slice(start, positions):
        """Creates a new linked list which is a slice of

        Args:
            start: starting node
            positions: number of positions to include in slice

        Returns:
            linked list which is a slice of a current one

        """
        # create a slice of a piece containing both sub-lists with preceding element
        slice_sub_array = SinglyLinkedList()
        node = start
        counter = 0
        while counter < positions and node:
            slice_sub_array.append(node.value)
            node = node.next
            counter += 1
        return slice_sub_array

    def replace(self, preceding_node, new_node) -> None:
        """Replace the node which is next to preceding with node

        Args:
            preceding_node: node that precedes the node which shall be replaced
            new_node: node to replace the node which is next to preceding

        Returns:
            None. All changes done in the given list.

        """
        if preceding_node:
            node_to_replace = preceding_node.next
            preceding_node.next = new_node
        else:
            node_to_replace = self.head
            self.head = new_node
        new_node.next = node_to_replace.next

    def sort(self) -> None:
        """Use iterative merge sort algorithm to order the elements by value

        Returns:
            None
        """
        length = self.get_length()
        sub_list_length = 1

        while sub_list_length < length:
            node_one = self.head
            pred_node_one = None

            """set markers of sub-lists to their starting positions"""
            for start_index in range(0, length, sub_list_length * 2):

                """create a slice containing first sub-list with preceding element"""
                slice_sub_first = SinglyLinkedList.slice(node_one, sub_list_length)

                # pred_node_two = pred_node_one
                node_two = node_one

                """move markers for second sub-list"""
                for _ in range(sub_list_length):
                    # pred_node_two = node_two
                    if not node_two:
                        break
                    node_two = node_two.next

                """create a slice containing second sub-list with preceding element"""
                slice_sub_second = SinglyLinkedList.slice(node_two, sub_list_length)

                # merge sub-lists
                """create markers for sub-arrays."""
                current_node_first_sub_list = slice_sub_first.head
                current_node_second_sub_list = slice_sub_second.head

                # iterate through the slices and put elements in order
                while current_node_first_sub_list and current_node_second_sub_list:

                    if current_node_second_sub_list.value <= current_node_first_sub_list.value:
                        # save the value of next because replace changes next
                        temp = current_node_second_sub_list.next
                        self.replace(pred_node_one, current_node_second_sub_list)
                        current_node_second_sub_list = temp
                    else:
                        temp = current_node_first_sub_list.next
                        self.replace(pred_node_one, current_node_first_sub_list)
                        current_node_first_sub_list = temp

                    # restore the value of node_one when its detached in case of head node
                    node_one = pred_node_one.next if pred_node_one else self.head
                    # move marker to the next position
                    pred_node_one = node_one
                    node_one = node_one.next

                """ensure that all remaining elements from first sub-list are merged"""
                while current_node_first_sub_list:
                    # save the value of next because replace changes next
                    temp = current_node_first_sub_list.next
                    self.replace(pred_node_one, current_node_first_sub_list)
                    current_node_first_sub_list = temp
                    pred_node_one = pred_node_one.next
                    node_one = node_one.next

                """ensure that all remaining elements from first sub-list are merged"""
                while current_node_second_sub_list:
                    # save the value of next because replace changes next
                    temp = current_node_second_sub_list.next
                    self.replace(pred_node_one, current_node_second_sub_list)
                    current_node_second_sub_list = temp
                    pred_node_one = pred_node_one.next
                    node_one = node_one.next

            sub_list_length *= 2


def create_from_list(array: list) -> SinglyLinkedList:
    linked_list = SinglyLinkedList()
    for element in array:
        linked_list.append(element)
    return linked_list
