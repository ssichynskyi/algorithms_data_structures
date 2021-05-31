from unittest import TestCase

from data_structures.my_queue import QueueConstTimeMaxEl, IllegalDequeueAttemptException
from helpers.execution_timer import get_execution_time
from helpers.randomized_arrays import get_random_array_of_ints


class TestQueueConstTimeMaxEl(TestCase):

    def test_enqueue_and_size(self):
        q = QueueConstTimeMaxEl()
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q._items[0], 1)

    def test_dequeue_and_init_with_basis(self):
        q = QueueConstTimeMaxEl([0])
        element = q.dequeue()
        self.assertEqual(element, 0)
        self.assertEqual(q.size(), 0)
        with self.assertRaises(IllegalDequeueAttemptException):
            q.dequeue()

    def test_get_max(self):
        q = QueueConstTimeMaxEl()
        q.enqueue(1)
        # [1] , 1
        self.assertEqual(q.get_max(), 1)
        q.enqueue(2)
        # [1,2], 2
        self.assertEqual(q.get_max(), 2)
        q.enqueue(3)
        # [1,2,3], 3
        self.assertEqual(q.get_max(), 3)
        q.enqueue(2)
        # [1,2,3,2], 3
        self.assertEqual(q.get_max(), 3)
        q.dequeue()
        # [2,3,2], 3
        self.assertEqual(q.get_max(), 3)
        q.dequeue()
        # [3,2], 3
        self.assertEqual(q.get_max(), 3)
        q.dequeue()
        # [2], 2
        self.assertEqual(q.get_max(), 2)
        q.enqueue(2)
        # [2,2], 2
        self.assertEqual(q.get_max(), 2)
        q.dequeue()
        # [2], 2
        self.assertEqual(q.get_max(), 2)
        q.enqueue(1)
        # [2,1], 2
        self.assertEqual(q.get_max(), 2)
        q.enqueue(4)
        # [2,1,4], 4
        self.assertEqual(q.get_max(), 4)
        q.dequeue()
        # [1,4], 4
        self.assertEqual(q.get_max(), 4)
        q.dequeue()
        # [4], 4
        self.assertEqual(q.get_max(), 4)
        q.dequeue()
        # [], None
        q.enqueue(1)
        # [1] , 1
        self.assertEqual(q.get_max(), 1)

    def test_amortization(self):
        q = QueueConstTimeMaxEl()
        for element in get_random_array_of_ints(100000, -10000, 10000):
            q.enqueue(element)
        _, time_hundred_thousand = get_execution_time(q.get_max)
        for element in get_random_array_of_ints(100, -10000, 10000):
            q.enqueue(element)
        _, time_hundred = get_execution_time(q.get_max)
        self.assertTrue(time_hundred_thousand/time_hundred < 30.0)
