#!usr/bin/python
# -*- coding: utf-8 -*-
from math import log10
from typing import Union


class NonIntegerElementInCountingSort(Exception):
    """ Exception is raised when counting sort is attempted on
    array containing other values than integers
    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def binary_search(sorted_list: list, searched_item) -> Union[int, None]:
    """Performs binary search in a given sorted list

    Args:
        sorted_list: a sorted list to look into
        searched_item: item to search for

    Returns:
        an index of the searched item or None if not found

    """
    lower = 0
    upper = len(sorted_list) - 1
    while upper >= lower:
        index = (upper + lower) // 2
        if sorted_list[index] == searched_item:
            return index
        else:
            if searched_item > sorted_list[index]:
                lower = index + 1
            else:
                upper = index - 1
    return None


def binary_search_recursive(sorted_list, searched_item, lower=None, upper=None) -> Union[int, None]:
    """Performs binary search in a given sorted list using recursion

    Args:
        sorted_list: a sorted list to look into
        searched_item: item to search for
        lower: lower bound of search. Used for recursion By default shall be None.
        upper: upper bound of search. Used for recursion By default shall be None.

    Returns:
        an index of the searched item or None if not found

    """
    if lower is None:
        lower = 0
    if upper is None:
        upper = len(sorted_list) - 1
    index = (lower + upper) // 2
    if sorted_list[index] == searched_item:
        return index
    if upper == lower:
        return None
    if searched_item > sorted_list[index]:
        return binary_search_recursive(sorted_list, searched_item, lower=index + 1, upper=upper)
    else:
        return binary_search_recursive(sorted_list, searched_item, lower=lower, upper=upper - 1)


def bubble_sort(array) -> None:
    """Implements the bubble sorting algorithm

    Note:
        This is ineffective O(n^2) sorting algorithm. O(1) by space
        Used mainly for educational purposes. In seldom best case
        can produce O(n) complexity
        Could be implemented in 2 variants: popping up and sinking
        This is an implementation of sinking

    Args:
        array: given array to sort

    Returns:
        None, changes are done directly in a given array

    """
    # The largest element will be pushed to the bottom in a first run,
    # so we won't have to come back to it
    max_index = len(array) - 1
    """only for performance improvement. len() is not calculated every time max index is referenced"""
    for n in range(max_index, 0, -1):
        for k in range(n):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]


def selection_sort(array) -> None:
    """Implements the selection sorting algorithm.

    Idea:
        Pass through the list and pick max (or min) item and place it
        into end (start) of the list

    Note:
        This is ineffective O(n^2) sorting algorithm. O(1) by space
        Used mainly for educational purposes

    Args:
        array: given array to sort

    Returns:
        None, changes are done directly in a given array

    """
    arr_length = len(array)
    """only for performance improvement. len() is not calculated every time max index is referenced"""
    for i in range(arr_length, 0, -1):
        max_index = 0
        for k in range(i):
            if array[k] > array[max_index]:
                max_index = k
        array[i - 1], array[max_index] = array[max_index], array[i - 1]


def insertion_sort(array) -> None:
    """Implements the insertion sorting algorithm

    Idea:
        Most left (right) side of the list is considered as already sorted list
        (starting from the 0th element which means sorted array of 1 element)
        One by one we add a new item from the rest (unsorted) part and put it into it

    Note:
        This is ineffective O(n^2) sorting algorithm. O(1) by space.
        Used mainly for educational purposes.
        In seldom best case can produce O(n) complexity

    Args:
        array: given array to sort

    Returns:
        None, changes are done directly in a given array

    """
    unsorted_lower_bound = 0
    arr_length = len(array)
    """only for performance improvement. len() is not calculated every time max index is referenced"""
    for i in range(1, arr_length):
        unsorted_lower_bound += 1
        """ stores an starting (smallest) index of the unsorted part of the array """
        # Code block below is not absolutely necessary, it's just for performance improvement
        # it ensures that we don't perform costly pop()-insert() when we don't need it
        if array[i] > array[i - 1]:
            continue
        # lower bound is -1 in order to reach 0th element
        # the faster alternative here is to implement a binary search to find the place to insert
        # it's also possible to improve execution time by starting from the higher bound in the upper
        # loop because popping up last element has O(1) time complexity. Still overall time complexity
        # will remain O(n^2) because insertion time complexity is O(n)
        for k in range(unsorted_lower_bound, -1, -1):
            if array[i] > array[k]:
                array.insert(k + 1, array.pop(i))
                break
        else:
            array.insert(0, array.pop(i))


def shell_sort(array: list) -> None:
    """Implements the shell sorting algorithm ver.1

    Idea:
        it's similar to insertion sort, but with the feature of
        selecting several sub-arrays (sorted)
        "Sub-array" is just a virtual array of elements that has the same distance
        between their indexes.
        For example: [15, 26, 71, 1, 16, 83, 42, 29] with distance == 3 will select
        following virtual arrays and sort them:
        1: [15, 1, 42]
        2: [26, 16, 29]
        3: [71, 83]
        Then it will exchange their positions like if these small lists are sorted:
        1: [1, 15, 42]
        2: [16, 26, 29]
        3: [71, 83]
        So, the end list will look like:
        [1, 16, 71, 15, 26, 83, 42, 29]
        Next step is to reduce the distance and repeat the process.
        The last stage is a simple insertion sort

    Note:
        implemented here is the binary one (not the most effective though)
        Time complexity varies from O(n*log(n)) to O(n*(log(n))^2) for optimized modifications
        Which makes it quite an effective algorithm from those that has O(1) memory complexity
        Although this implementation looks as if it has high time complexity because of 4 nested loops,
        it provides the expected performance of ~ n*log(n). According to measurements the execution time
        is increased by factor ~ 230 when n is increased 100 times. The reason is that all nested loops
        has time complexity less than O(N), mostly log(N)

    Args:
        array: array to sort

    Returns:
        None, changes are done directly in a given array

    """

    max_index = len(array) - 1
    """int: only for performance improvement. len() is not calculated every time max index is referenced"""
    distance = len(array) // 2
    """int: select the distance between elements (use binary although it's not the most effective one)"""
    while distance >= 1:
        for i in range(0, distance):
            """create a virtual sub-array which members have equal distance from one another
            and sort them using the principle of insertion sort (left part considered sorted).
            Here i is a counter for these virtual sub-arrays 
            """
            for j in range(i + distance, max_index + 1, distance):
                """i + distance - is an index of a second element in virtual sub-array
                first element in this virtual sub-array has index 'i'.
                We start from the second one since first element represents an already sorted
                sub-sub-array
                """
                current_index = j
                """j is only the starting value, to proceed with comparison with previous
                elements of a virtual array, index is used.
                Current_index tracks the position of initial a[j] element during all changes in it's
                position during sorting
                """
                for k in range(j - distance, i - 1, -distance):
                    if array[current_index] < array[k]:
                        array[current_index], array[k] = array[k], array[current_index]
                        current_index = k
                    else:
                        """array is guaranteed to be sorted, so once we discover an element smaller,
                        than array[j], it makes no sense to proceed
                        """
                        break
        distance //= 2


def merge_sort(array):
    """Implementation of the merge-sorting algorithm.

    Idea:
        array is split in two parts recursively until arrays with length == 1 remain.
        Then they are one-by-one merged in ascending order:

    Example of merge algorithm for 2 arrays, which at this stage are already sorted
        because the same process was done 1 step ago with [1],[2] and [0],[2]:
        left_array = [1 , 2], right_array = [0, 2]
        array = [1 , 2, 0, 2]
        i - counter for the left array
        j - counter for the right array
        k - counter for array
        i,j,k = 0
        / Below counter values are showed for the end of the step /
        1: i = 0, j = 0, k = 0: array = [0, 2, 0, 2], i=0, j=1, k=1
        2: i = 0, j = 0, k = 0: array = [0, 1, 0, 2], i=1, j=1, k=2
        3: i = 0, j = 0, k = 0: array = [0, 1, 2, 2], i=1, j=2, k=3
        4: i = 0, j = 0, k = 0: array = [0, 1, 2, 2], i=1, j=2, k=4

    Args:
        array: array to sort

    Returns:
        None, changes are done in an input array

    """
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]
        """split array on 2 sub-arrays"""

        merge_sort(left_array)
        merge_sort(right_array)
        """ recursively call merge for all sub-parts """

        i, j, k = 0, 0, 0
        """code below will start execution only when the bottom (array with len == 1) is reached"""
        while i < len(left_array) and j < len(right_array):
            """perform merge of left_array with right_array"""
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            """this cycle ensure that the remaining elements of left_array are also merged into array"""
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            """this cycle ensure that the remaining elements of right_array are also merged into array"""
            array[k] = right_array[j]
            j += 1
            k += 1


def merge_sort_multi_adapted(array):
    """Variation of merge sort adapted for multi-processing

    Args:
        array: list to sort

    Returns:
        sorted list
    """
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
    left_array = merge_sort_multi_adapted(array[:mid])
    right_array = merge_sort_multi_adapted(array[mid:])
    return merge(left_array, right_array)


def merge(left_array, right_array):
    """Merge two sorted lists into one sorted list

    Note:
        this function is a helper method for merge sort.
        It doesn't work correctly with unsorted input params.
        Implemented as a public function because of usage in
        multiprocess modification of a merge sort.

    Args:
        left_array: sorted list
        right_array: sorted list

    Returns:
        sorted list which consists of all elements passed as parameters

    """
    i, j = 0, 0
    result = []
    while True:
        if i >= len(left_array):
            result.extend(right_array[j:])
            break
        if j >= len(right_array):
            result.extend(left_array[i:])
            break
        if left_array[i] <= right_array[j]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1
    return result


def quick_sort(array, start=None, stop=None):
    """Implements quick sort algorithm.

    Idea:
        Recursive, top-down algorithm with typical time performance O(N*log(N))
        and worst-case performance O(N^2)

        1. Arbitrary pivot element is taken
        2. In the virtual array that represents initial array minus pivot element
        we start moving left marker from most left element and right marker from
        the most right element
        3. We stop left marker when we find an element with a value greater or equal than pivot
        4. We stop right marker when we find an element with value less than a pivot
        5. Once both markers stopped we exchange the elements
        6. Then we move the pivot value to a point where markers have met.
        7. Then split parts of the array on left (to a pivot) and right (to a pivot) and apply
        quick_sort recursively in the same manner.

    Args:
        array: array to sort
        start: index of sub-array to start from. Only for recursion. Shall be not given on a first call.
        stop: index of sub-array to finish at. Shall be not given on a first call

    Returns:
        None, all changes are done directly in a given array

    """

    if start is None:
        start = 0
    if stop is None:
        stop = len(array) - 1
    """statements above are used only in the first run"""

    if start >= stop:
        return
    """if array have len == 1, it's sorted by default. Recursion trivial case."""

    pivot_index = start
    """setting pivot element. By default it's the 0th element of given array / sub-array"""

    low_index, high_index = pivot_index + 1, stop
    """since we select first element as a pivot index, low index is selected as first element above it"""

    while high_index > low_index:
        """searching for the first occurrence of the element on the LEFT, which is GREATER than pivot"""
        while array[low_index] < array[pivot_index] and high_index > low_index:
            low_index += 1
        """searching backwards for the first occurrence of the element on the RIGHT, which is LOWER than pivot"""
        while array[high_index] >= array[pivot_index] and high_index > low_index:
            high_index -= 1
        if array[low_index] >= array[pivot_index] > array[high_index]:
            array[low_index], array[high_index] = array[high_index], array[low_index]

    if array[low_index] < array[pivot_index]:
        array.insert(low_index, array.pop(pivot_index))
        pivot_index = low_index
    else:
        array.insert(low_index - 1, array.pop(pivot_index))
        pivot_index = low_index - 1
    """above the right place for the pivot element is searched"""

    quick_sort(array, start=start, stop=max(pivot_index - 1, start))
    quick_sort(array, start=min(pivot_index + 1, stop), stop=stop)
    """recursively sort sub-arrays"""


def counting_sort(array):
    """Implements counting sort

    Note:
        High performance algorithm for sorting integers. Especially effective for
        large amounts of small integers. Time performance O(n+k+l). Memory O(k+l).
        Where k and l are the maximum absolute value the max positive and max negative element
    Args:
        array: array to be sorted. Must consist of only integer elements

    Raises:
        NonIntegerElementInCountingSort

    Returns:
        None, all changes are done directly in a given array

    """
    if len(array) == 0:
        return
    if array is None:
        raise ValueError('Array under sorting cannot be None')
    max_value = max(array)
    min_value = min(array)
    """the code above could be slightly optimized by introducing a custom function
    that will collect max and min values simultaneously
    """
    array_of_positives = [0] * (max_value + 1)
    array_of_negatives = [0] * (-min_value + 1)

    for element in array:
        if element < 0:
            try:
                array_of_negatives[-element] += 1
            except IndexError:
                raise NonIntegerElementInCountingSort(
                    'Counting sort cannot perform on non-integer values'
                )
        else:
            try:
                array_of_positives[element] += 1
            except IndexError:
                raise NonIntegerElementInCountingSort(
                    'Counting sort cannot perform on non-integer values'
                )
    """collect elements into two arrays according to their sign. 0 is considered as positive"""

    current_index = 0
    for i in range(len(array_of_negatives) - 1, -1, -1):
        for j in range(array_of_negatives[i]):
            array[current_index] = -i
            current_index += 1
    for i in range(len(array_of_positives)):
        for j in range(array_of_positives[i]):
            array[current_index] = i
            current_index += 1
    """above for loops reconstructs the array that is already sorted"""


def radix_sort(array: list, max_rank=None, current_rank=None):
    """Implements radix / bucket sorting algorithm

    Idea:
        elements are put into buckets according to the value of their
        MSN/LSN (most/least significant number). There's alternative
        with bit-by-bit comparison. But since in python bit operations
        are not very fast, it makes little sense.

    Note:
        In general, this is a high performance algorithm which works
        for all kinds of data, which could be lexicographically ordered.
        This implementation is done only for the list of integers.
        Time complexity O(n*k) where k is a max number of bits in array
        elements

    Args:
        array: array to be sorted.
        max_rank: max rank of the integer in the array. Shall be None if not known.
        current_rank: used for recursive calls. Shall be None on initial call

    Returns:
        None, all changes are done directly in a given array
        But during recursive calls it does return lists

    """
    if len(array) <= 1:
        return array
    if array is None:
        raise ValueError('Array under sorting cannot be None')

    # code below is executed not more than one time
    if max_rank is None:
        max_value = max(array)
        min_value = min(array)

        if max_value > 0:
            rank_of_max = int(log10(max_value))
        elif max_value < 0:
            rank_of_max = int(log10(-max_value))
        else:
            rank_of_max = 1
        """get rank / number of digits in max. element of the array"""
        if min_value > 0:
            rank_of_min = int(log10(min_value))
        elif min_value < 0:
            rank_of_min = int(log10(-min_value))
        else:
            rank_of_min = 1
        """get rank / number of digits in min. element of the array"""
        max_rank = max(rank_of_min, rank_of_max)

    # Code below is executed only on initial iteration
    if current_rank is None:
        current_rank = max_rank
        array_of_positives = []
        array_of_negatives = []
        for element in array:
            if element >= 0:
                array_of_positives.append(element)
            else:
                array_of_negatives.append(element)
        array_of_positives = radix_sort(array_of_positives, max_rank, current_rank)
        array_of_negatives = radix_sort(array_of_negatives, max_rank, current_rank)
        """below is the place of final exit"""
        array.clear()
        array.extend(array_of_negatives[:] + array_of_positives[:])
        return

    if current_rank > 0:
        temp_array = [[], [], [], [], [], [], [], [], [], []]
        for element in array:
            temp_array[(element // 10 ** current_rank) % 10].append(element)
        for i in range(len(temp_array)):
            temp_array[i] = radix_sort(temp_array[i], max_rank=max_rank, current_rank=current_rank-1)
        # merge sub-lists into list
        return [element for sub_array in temp_array for element in sub_array]
    else:
        # In trivial case the sorting of minimal bucket is done using any other algorithm
        insertion_sort(array)
        return array


def heap_sort(array: list) -> None:
    """Sorts the array using a binary heap (prioritized queue)

    Note:
        binary heap is a complete binary tree (filled with no spaces),
        where nodes below the current have lower (bigger) value.
        Some data:
            [14, 12, 10, 8, 5, 9, 4] - is a way to store the BH
            if current node has index i, then it's leaves (child) node indexes are:
            left = 2*i + 1
            right = 2*i + 2
            The index of the last node with children is therefore = (n - 1s) // 2,
            where n is the last index of the bin-heap list (e.g. len(array) - 1)
        This algorithm has a constant time performance N*log(N) and O(1) space performance

    Idea:
        Take the last node with leaves (children) and apply heapify on it.
        Heapify is a process of bringing the elements below the current node
        into the binary heap order (parent node > child nodes)
        Repeat the process by moving left in the heap array.

    Args:
        array: array to sort

    Returns:
        None, all changes are done directly in a given array

    """
    def heapify(array: list, max_index: int, i: int) -> None:
        """Self-implemented heapify.

        Note:
            In a python module heapq there's a full implementation of related functions.
            So, this is implemented to get better understanding

        Args:
            array: array to heapify
            max_index: maximal index of the array that shall be heapified (e.g. stop point)
            i: the starting index (index of a root element, e.g. starting point)

        Returns:
            None, changes are done in a provided parameter

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
            heapify(array, max_index, index_of_min)

    # Here array is transformed to a binary heap:
    max_index = len(array) - 1
    for i in range((max_index - 1) // 2, -1, -1):
        heapify(array, max_index, i)
    """above: start from the latest node with leaves and proceed up to the root node.
    
    At this stage array represents a binary heap. However it's not a sorted list yet.
    Because bin heap doesn't provide any rule about left node < right node
    """

    """The idea of the loop below - to take the smallest element(root) put it to the end and
    heapify all elements from 0 to max_index - 1. Proceed until the last element.
    In this case all list is already sorted.
    """
    for i in range(max_index, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i - 1, 0)
