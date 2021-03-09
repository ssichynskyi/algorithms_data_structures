#!usr/bin/python
# -*- coding: utf-8 -*-

from data_structures.stack import Stack
from data_structures.my_queue import Queue


class BinaryTreeNode:
    """Implementation of the binary tree node

    Idea:
        binary tree is a form of a tree data structure which node has only 2 children:
        left and right.

    Args:
        root_obj: an object / tree node which takes a role of a root node

    """

    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node, decision_func=None) -> None:
        """Add new node as a left child

        Idea:
            inserts the node as a left child. If the node already has
            left child, decide which child (left/right) it shall become using
            decision_func.
        Args:
            new_node: tree node (a key) to add
            decision_func: function which makes a decision if a new node shall
            be a left or right child. Result 0/False means left child, 1/True - right.
            If decision_func is None, left child is chosen.
            Decision_func shall take 2 parameters, new_node and left child

        Returns:
            None

        """
        if self.left_child is None:
            self.left_child = new_node
        else:
            tree_node = BinaryTreeNode(new_node)
            if decision_func is None:
                def decision_func(x, y): return 0
        if decision_func(new_node, self.key):
            tree_node.left_child = self.left_child
        self.left_child = tree_node

    def insert_right(self, new_node, decision_func=None) -> None:
        """Add new node as a right child

        Idea:
            inserts the node as a right child. If the node already has
            right child, decide which child (left/right) it shall become using
            decision_func.
        Args:
            new_node: tree node (a key) to add
            decision_func: function which makes a decision if a new node shall
            be a left or right child. Result 0/False means left child, 1/True - right.
            If decision_func is None, right child is chosen.
            Decision_func shall take 2 parameters, new_node and right child

        Returns:
            None

        """
        if self.right_child is None:
            self.right_child = new_node
        else:
            tree = BinaryTreeNode(new_node)
            tree.right_child = self.right_child
            self.right_child = tree

    def get_left_child(self) -> object:
        return self.left_child

    def get_right_child(self) -> object:
        return self.right_child

    def set_root_value(self, value) -> None:
        self.key = value

    def get_root_value(self) -> None:
        return self.key
