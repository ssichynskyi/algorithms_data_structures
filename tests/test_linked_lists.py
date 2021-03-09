from unittest import TestCase
from data_structures.linked_lists import SinglyLinkedList, create_from_list


class Test(TestCase):
    def test_create_from_list(self):
        array = [2, 1, 'a']
        test_sll = create_from_list(array)
        node = test_sll.head
        for i in range(0, len(array)):
            self.assertEqual(array[i], node.value)
            node = node.next

    def test_singly_linked_list_init(self):
        test_sll = SinglyLinkedList()
        self.assertEqual(SinglyLinkedList, type(test_sll))
        self.assertEqual(test_sll.head, None)
        with self.assertRaises(TypeError):
            SinglyLinkedList('abc')

    def test_singly_linked_list_append(self):
        test_sll = SinglyLinkedList()
        test_values = (1, 2)
        test_sll.append(test_values[0])
        self.assertEqual(test_sll.head.value, test_values[0])
        self.assertEqual(test_sll.head.next, None)
        test_sll.append(test_values[1])
        self.assertEqual(test_values[0], test_sll.head.value)
        self.assertEqual(test_values[1], test_sll.head.next.value)

    def test_singly_linked_list_push(self):
        test_sll = SinglyLinkedList()
        test_values = (1, 2)
        test_sll.push(test_values[0])
        self.assertEqual(test_values[0], test_sll.head.value)
        test_sll.push(test_values[1])
        self.assertEqual(test_values[1], test_sll.head.value)

    def test_singly_linked_list_cycled(self):
        test_sll = SinglyLinkedList()
        test_sll.append('x')
        test_sll.append('y')
        self.assertFalse(test_sll.is_linked_list_cycled())
        """make a cycled list"""
        test_sll.head.next.next = test_sll.head
        self.assertTrue(test_sll.is_linked_list_cycled())

    def test_singly_linked_list_values_to_list(self):
        test_sll = SinglyLinkedList()
        test_sll.append('x')
        test_sll.append('y')
        self.assertTupleEqual(('x', 'y'), tuple(test_sll.values_to_list()))

    def test_singly_linked_list_reversal(self):
        test_sll = SinglyLinkedList()
        test_sll.append('x')
        test_sll.append('y')
        self.assertEqual('x', test_sll.head.value)
        self.assertEqual('y', test_sll.head.next.value)
        test_sll.reverse()
        self.assertEqual('y', test_sll.head.value)
        self.assertEqual('x', test_sll.head.next.value)

    def test_singly_linked_list_length(self):
        test_sll = SinglyLinkedList()
        test_sll.append('x')
        test_sll.append('y')
        self.assertEqual(2, test_sll.get_length())
        self.assertEqual(2, test_sll.get_length(test_sll.head))
        self.assertEqual(1, test_sll.get_length(test_sll.head.next))

    def test_singly_linked_list_sort(self):
        array = [2, 1, 7, 9, 5, 3, 0, 1, 12, -4, 1]
        test_sll = create_from_list(array)
        array.sort()
        test_sll.sort()
        node = test_sll.head
        for element in array:
            self.assertEqual(element, node.value)
            node = node.next
