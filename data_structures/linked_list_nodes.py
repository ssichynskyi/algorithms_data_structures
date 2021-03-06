#!usr/bin/python
# -*- coding: utf-8 -*-


class SingleListNode:
    """Node for a singly linked list"""
    def __init__(self, value):
        self.next = None
        self.value = value


class DoublyLinkedListNode:
    """Node for a doubly linked list"""
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value


class IllegalLinkedListOperation(Exception):
    """General exception for illegal operations with linked lists"""
    def __init__(self, *args):
        Exception.__init__(self, *args)
