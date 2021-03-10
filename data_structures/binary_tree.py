#!usr/bin/python
# -*- coding: utf-8 -*-

from data_structures.stack import Stack
from data_structures.my_queue import Queue


class BinaryTreeNode:
    """Implementation of the binary tree / binary tree node

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
        """Add new node as a child using a rule

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
        """Add new node as a left child

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
        """Add new node as a right child

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
        """Traverse the binary tree in-order

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
        """Traverse the binary tree pre-order

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
        """Traverse the binary tree post-order

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
