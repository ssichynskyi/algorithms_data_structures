from unittest import TestCase

from data_structures.stack import StackConstTimeMaxEl, IllegalPopAttemptException
from helpers.randomized_arrays import get_random_array_of_ints
from helpers.execution_timer import get_execution_time


class TestStackConstTimeMaxEl(TestCase):

    def test_init(self):
        test_stack = StackConstTimeMaxEl()
        self.assertEqual(len(test_stack._items), 0)
        self.assertIsNone(test_stack.get_max())

    def test_push(self):
        test_stack = StackConstTimeMaxEl()
        test_stack.push(1)
        self.assertEqual(len(test_stack._items), 1)
        self.assertEqual(test_stack._items[0], 1)
        self.assertEqual(len(test_stack._max_value_stack._items), 1)
        self.assertEqual(test_stack._max_value_stack._items[0], 1)

    def test_pop(self):
        test_stack = StackConstTimeMaxEl()
        with self.assertRaises(IllegalPopAttemptException):
            test_stack.pop()
        test_stack = StackConstTimeMaxEl([-1])
        self.assertEqual(test_stack.pop(), -1)
        test_stack = StackConstTimeMaxEl([0, 2])
        test_stack.pop()
        self.assertEqual(len(test_stack._max_value_stack._items), 1)
        self.assertEqual(test_stack._max_value_stack._items[0], 0)

    def test_get_max(self):
        test_stack = StackConstTimeMaxEl()
        test_stack.push(1)
        # [1] [1]
        self.assertEqual(test_stack.get_max(), 1)
        test_stack.push(2)
        # [1,2] [1,2]
        self.assertEqual(test_stack.get_max(), 2)
        test_stack.push(1)
        # [1,2,1] [1,2]
        self.assertEqual(test_stack.get_max(), 2)
        test_stack.push(2)
        # [1,2,1,2] [1,2,2]
        self.assertEqual(test_stack.get_max(), 2)
        test_stack.push(2)
        # [1,2,1,2,2] [1,2,2,2]
        self.assertEqual(test_stack.get_max(), 2)
        test_stack.push(3)
        # [1,2,1,2,2,3] [1,2,2,2,3]
        self.assertEqual(test_stack.get_max(), 3)
        test_stack.push(-5)
        # [1,2,1,2,2,3,-5] [1,2,2,2,3]
        self.assertEqual(test_stack.get_max(), 3)
        test_stack.pop()
        # [1,2,1,2,2,3] [1,2,2,2,3]
        self.assertEqual(test_stack.get_max(), 3)
        test_stack.pop()
        # [1,2,1,2,2] [1,2,2,2]
        self.assertEqual(test_stack.get_max(), 2)
        test_stack.pop()
        # [1,2,1,2] [1,2,2]
        self.assertEqual(test_stack.get_max(), 2)
        test_stack.pop()
        # [1,2,1] [1,2]
        self.assertEqual(test_stack.get_max(), 2)
        test_stack.pop()
        # [1,2] [1,2]
        self.assertEqual(test_stack.get_max(), 2)
        test_stack.pop()
        # [1] [1]
        self.assertEqual(test_stack.get_max(), 1)

    def test_amortization(self):
        test_stack = StackConstTimeMaxEl()
        for element in get_random_array_of_ints(100000, -10000, 10000):
            test_stack.push(element)
        result, time_hundred_thousand = get_execution_time(test_stack.get_max)
        for element in get_random_array_of_ints(100, -10000, 10000):
            test_stack.push(element)
        result, time_hundred = get_execution_time(test_stack.get_max)
        print(time_hundred)
        print(time_hundred_thousand)
        self.assertTrue(time_hundred_thousand/time_hundred < 30.0)
