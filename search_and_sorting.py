#!usr/bin/python
# -*- coding: utf-8 -*-
from typing import Union


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
        return binary_search_recursive(sorted_list, searched_item, lower=index+1, upper=upper)
    else:
        return binary_search_recursive(sorted_list, searched_item, lower=lower, upper=upper-1)


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
    max_index = len(array) - 1
    """only for performance improvement. len() is not calculated every time max index is referenced"""
    for i in range(max_index, 0, -1):
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
    max_index = len(array) - 1
    """only for performance improvement. len() is not calculated every time max index is referenced"""
    for i in range(1, max_index):
        unsorted_lower_bound += 1
        """ stores an starting (smallest) index of the unsorted part of the array """
        # Code block below is not absolutely necessary, it's just for performance improvement
        # it ensures that we don't perform costly pop()-insert() when we don't need it
        if array[i] > array[i - 1]:
            continue
        # lower bound is -1 in order to reach 0th element
        # the faster alternative here is to implement a binary search to find the place to insert
        # it's also possible to improve execution time by starting from the higher bound in the upper
        # loop because poping up last element has O(1) time complexity. Still overall time complexity
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
        For example: [15, 26, 71, 1, 16, 83, 42, 29] with increment == 3 will select
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
        Next step is to reduce the increment and repeat the process.
        The last stage is a simple insertion sort

    Note:
        implemented here is the binary one (not the most effective though)
        Time complexity varies from O(n*log(n)) to O(n*(log(n))^2) for optimized modifications
        Which makes it quite an effective algorithm from those that has O(1) memory complexity

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


def shell_sort_2(array: list) -> None:
    """Implements the shell sorting algorithm ver.2.

    This is copied from the internet and improved solution.
    Improvement is not related to performance, just readability and simplicity

    Idea:
        it's similar to insertion sort, but with the feature of
        selecting several sub-arrays (sorted)
        "Sub-array" is just a virtual array of elements that has the same distance
        between their indexes.
        For example: [15, 26, 71, 1, 16, 83, 42, 29] with increment == 3 will select
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
        Next step is to reduce the increment and repeat the process.
        The last stage is a simple insertion sort

    Note:
        implemented here is the binary one (not the most effective though)
        Time complexity varies from O(n*log(n)) to O(n*(log(n))^2) for optimized modifications
        Which makes it quite an effective algorithm from those that has O(1) memory complexity

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
        for i in range(distance, max_index + 1):
            """add a[i] to the elements that have been sorted by insertion
            shift earlier sorted elements up until the correct location for a[i] is found
            """
            for j in range(i, distance-1, -distance):
                if array[j] < array[j-distance]:
                    array[j], array[j-distance] = array[j-distance], array[j]
        distance //= 2


def merge_sort(array):
    """Implementation of the merge-sorting algorithm.

    Args:
        array: array to sort

    Returns:
        None, changes are done in an input array
    """
    if len(array) > 1:
        mid = len(array) // 2
        # split out array on 2 sub-arrays
        left_array = array[:mid]
        right_array = array[mid:]

        # recursively call merge for all sub-parts
        merge_sort(left_array)
        merge_sort(right_array)

        # this part will start execution only when the bottom (array with len == 1) is reached
        i, j, k = 0, 0, 0
        # perform merge of left_array with right_array
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        # this cycle ensure that the remaining elements of left_array are also merged into array
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        # this cycle ensure that the remaining elements of right_array are also merged into array
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1


def quick_sort(array, start=None, stop=None):
    """
    Implements quick sort algorithm.
    The essence of the quicksort is following:
    1. Arbitrary pivot element is taken
    2. In the virtual array that represents initial array minus pivot element we start moving left marker
    from most left element and right marker from most right element
    3. We stop left marker when we find an element with a value greater or equal than pivot
    4. We stop right marker when we find an element with value less than a pivot
    5. Once both markers stopped we exchange the elements
    6. Then we move the pivot value to a point where markers have met.
    7. Then split parts of the array on left (to a pivot) and right (to a pivot) and apply quick_sort recursively
    in the same manner.
    :param array: array to sort
    :param start: index of sub-array to start from. Only for recursion. Normally shall be not given on a first call
    :param stop: index of sub-array to finish at. Normally shall be not given on a first call
    :return: None, all changes are done directly in a given array
    """
    # statements below are used only in the first run
    if start is None:
        start = 0
    if stop is None:
        stop = len(array) - 1
    # if array have len == 1, it's sorted by default. Recursion trivial case.
    if start >= stop:
        return
    # setting pivot element. By default it's the 0th element of given array / sub-array
    pivot_index = start
    low_index, high_index = pivot_index + 1, stop

    while high_index > low_index:
        # searching for the first occurrence of the element on the LEFT, which is GREATER than pivot
        while array[low_index] < array[pivot_index] and high_index > low_index:
            low_index += 1
        # searching backwards for the first occurrence of the element on the RIGHT, which is LOWER than pivot
        while array[high_index] >= array[pivot_index] and high_index > low_index:
            high_index -= 1
        if array[low_index] >= array[pivot_index] > array[high_index]:
            array[low_index], array[high_index] = array[high_index], array[low_index]
    # insert the pivot element into the right place
    if array[low_index] < array[pivot_index]:
        array.insert(low_index, array.pop(pivot_index))
        pivot_index = low_index
    else:
        array.insert(low_index - 1, array.pop(pivot_index))
        pivot_index = low_index - 1
    # execute recursively for the left and right sub-arrays
    quick_sort(array, start=start, stop=max(pivot_index - 1, start))
    quick_sort(array, start=min(pivot_index + 1, stop), stop=stop)
