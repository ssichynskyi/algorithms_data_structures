#!usr/bin/python
# -*- coding: utf-8 -*-


class BinaryTree:
    """Implementation of the binary tree / binary tree node.

    Idea:
        binary tree is a form of a tree data structure which node has only 2 children:
        left and right.

    Args:
        root_obj: an object / tree node which takes a role of a root node

    """

    def __init__(self, root_obj):
        self._key = root_obj
        self._left_child = None
        self._right_child = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def left_child(self):
        return self._left_child

    @property
    def right_child(self):
        return self._right_child

    def insert(self, new_node, rule) -> None:
        """Add new node as a child using a rule.

        Idea:
            inserts the node as a child using the rule(self, new_node)

        Args:
            new_node: tree node (a _key) to add
            rule: function that determines if a new_node shall be a left or right child.
            Result 0/False means left child, 1/True - right. Shall take 2 params:
            - new node (new_node)
            - root node (self)

        Returns:
            None

        """
        child = '_left_child' if rule(self, new_node) else '_right_child'

        if getattr(self, child):
            setattr(new_node, child, getattr(self, child))
        setattr(self, child, new_node)

    def insert_left(self, new_node) -> None:
        """Add new node as a left child.

        Idea:
            inserts the node as a left child. If the node already has
            left child, make it a left child of the new node
        Args:
            new_node: tree node (a _key) to add

        Returns:
            None

        """
        self.insert(new_node, lambda root, new: False)

    def insert_right(self, new_node) -> None:
        """Add new node as a right child.

        Idea:
            inserts the node as a right child. If the node already has
            right child, make it a right child of the new node

        Args:
            new_node: tree node (a _key) to add

        Returns:
            None

        """
        self.insert(new_node, lambda root, new: True)

    def inorder_traversal(self, node) -> list:
        """Traverse the binary tree in-order.

        Note:
            in-order means we visit and record left child, then root and then right child.
            In-order traversal of BST will return a sorted list.

        Args:
            node: a tree node from which to start traversal

        Returns:
            A list of node values

        """
        result = []
        if node:
            result.extend(self.inorder_traversal(node.left))
            result.append(node.key)
            result.extend(self.inorder_traversal(node.right))
        return result

    def preorder_traversal(self, node) -> list:
        """Traverse the binary tree pre-order.

        Note:
            pre-order means we visit and record root, then left child and at last right child.

        Args:
            node: a tree node from which to start traversal

        Returns:
            A list of node values

        """
        result = []
        if node:
            result.append(node.key)
            result.extend(self.inorder_traversal(node.left))
            result.extend(self.inorder_traversal(node.right))
        return result

    def postorder_traversal(self, node) -> list:
        """Traverse the binary tree post-order.

        Note:
            post-order means we visit and record left child, then right child and at last root

        Args:
            node: a tree node from which to start traversal

        Returns:
            A list of node values

        """
        result = []
        if node:
            result.extend(self.inorder_traversal(node.left))
            result.extend(self.inorder_traversal(node.right))
            result.append(node.key)
        return result


class BinHeap:
    """Implements binary heap tree.

    Idea:
        binary heap is a binary tree where every child is
        smaller (bigger) than it's parent

    Args:
         input_list: list from which BinHeap shall be build

    """
    def __init__(self, input_list=None):
        if input_list is None:
            input_list = list()
        self._heap_list = input_list
        # number of nodes in the tree
        self._size = len(input_list)

    @property
    def heap_list(self):
        return self._heap_list

    @property
    def size(self):
        return self._size

    def build_heap(self, input_list: list) -> None:
        """Rewrites binary heap with a one made from a given list.

        Note:
            Unlike constructor method, it accepts normal list
            and sorts it out as a heap.
        Args:
            input_list: unordered list

        Returns:
            None. Updates existing bin heap

        """
        # apply perc_up() starting from  the last node with leaves
        self._size = len(input_list)
        self._heap_list = input_list
        max_index = len(self._heap_list) - 1
        for i in range((max_index - 1) // 2, -1, -1):
            self._perc_down(self._heap_list, max_index, i)
        """above: start from the latest node with leaves and proceed up to root node."""

    def _perc_down(self, array: list, max_index: int, i: int) -> None:
        """Push element through the entire path to the max_index.

        Note:
            In a python module heapq there's a full implementation of related functions.
            So, this is implemented to get better understanding

        Args:
            array: array to heapify
            max_index: maximal index of the array that shall be heapified
            i: the starting index (index of a root element, e.g. starting point)

        Returns:
            None, changes are done in a provided array parameter

        """
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        index_of_min = i
        if left_index <= max_index and array[left_index] > array[index_of_min]:
            index_of_min = left_index
        if right_index <= max_index and array[right_index] > array[index_of_min]:
            index_of_min = right_index
        """code above discovers the node which has min value within root, left node, right node"""
        if index_of_min != i:
            array[index_of_min], array[i] = array[i], array[index_of_min]
            """perform similar operation recursively for all children of the moved node"""
            self.heapify(array, max_index, index_of_min)

    # def perc_up(self, i) -> None:
    #     """Push element through the entire path to the root
    #
    #     Note:
    #         method will update the entire branch.
    #         The process is started from the last node with at least one leave
    #     Args:
    #         i: index of the element
    #
    #     Returns:
    #         None
    #
    #     """
    #     while i // 2 > 0:
    #         if self._heap_list[i] < self._heap_list[i // 2]:
    #             self._heap_list[i], self._heap_list[i // 2] = self._heap_list[i // 2], self._heap_list[i]
    #         i //= 2

    # def insert(self, value) -> None:
    #     """Inserts the element to it's place
    #
    #     Note:
    #         Inserts the element to the end of the list and
    #         propagates it until the next up to the root node
    #
    #     Args:
    #         value: value of the inserted element
    #
    #     Returns:
    #         None
    #
    #     """
    #     self.heap_list.append(value)
    #     self.size += 1
    #     self.perc_up(self.size)

    def perc_down(self, i) -> None:
        """
        Push element down to the leaves through the entire path and updates the branch
        :param i: index of the element to push
        :return: None
        """
        while i < self.size:
            min_child_index = self.min_child(i)
            if self.heap_list[i] > self.heap_list[min_child_index]:
                self.heap_list[i], self.heap_list[min_child_index] = self.heap_list[min_child_index], self.heap_list[i]
            i = min_child_index

    def min_child(self, i) -> int:
        """
        Get child with minimal value of the i-th node
        :param i: index of the node to address
        :return: the index of the child node with a minimal value
        """
        if 2 * i + 1 > self.size:
            return 2 * i
        return 2 * i if self.heap_list[2 * i] < self.heap_list[2 * i + 1] else 2 * i + 1

    def del_root(self):
        """
        Also del_min() as our root is a node with a minimum.
        Crucial part of this operation is to get new root and restore the heap order.
        This is done in a following way: we push last node to a root position and then
        push it down using perc_down() method
        :return: the value of the removed node
        """
        min_node = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.heap_list.pop()
        self._size -= 1
        self.perc_down(1)
        return min_node


def bst_rule(root_node, new_node) -> bool:
    """A rule for a binary search tree"""
    return False if new_node.key > root_node.key else True


def bin_heap_desc_rule(root_node, new_node) -> bool:
    """A rule for a descending binary heap"""
    if new_node.key > root_node.key:
        raise ValueError('In descending binary heap the child node shall be not bigger than root')
    return _bin_heap_rule(root_node)


def bin_heap_asc_rule(root_node, new_node) -> bool:
    """A rule for an ascending binary heap"""
    if new_node.key > root_node.key:
        raise ValueError('In ascending binary heap the child node shall be not smaller than root')
    return _bin_heap_rule(root_node)


def _bin_heap_rule(root_node) -> bool:
    if not root_node.left_child:
        return False
    if not root_node.right_child:
        return True
    return False
