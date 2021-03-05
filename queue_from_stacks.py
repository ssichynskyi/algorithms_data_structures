from data_structures.stack import Stack

""" Implement a Queue - Using Two Stacks
Given the Stack class below, implement a Queue class using two stacks! 
"""


class QueueOutOfStack:
    """Implements queue of two stacks

    Idea:
        1st stack for input, 2nd for output.
        While enqueue is called, data is stored in the input stack
        Once dequeue is called it gets data from the output stack until
        it's empty. If dequeue is called on empty output stack,
        all data from input stack is flush to the output stack.
    """
    def __init__(self):
        self.input_stack = Stack()
        self.output_stack = Stack()

    def is_empty(self):
        return self.input_stack.is_empty() and self.output_stack.is_empty()

    def enqueue(self, item):
        self.input_stack.push(item)

    def dequeue(self):
        if self.output_stack.is_empty():
            while not self.input_stack.is_empty():
                self.output_stack.push(self.input_stack.pop())
        return self.output_stack.pop()
