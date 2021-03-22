from collections import UserList


def find_median_of_two_sorted_lists(nums1: list, nums2: list) -> float:
    """Finds the median of two sorted lists when they are merged

    Note:
        solution provides less, than O(n) time complexity.
        Need to clarify why not log(n).
        Getting O(n+m) time complexity is not tricky.
        Merge function of a merge sort will do it.

    Args:
        nums1: sorted list of digits
        nums2: sorted list of digits

    Returns:
        the median value of nums1 and nums2 when merged

    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    """make nums2 largest of 2 arrays"""

    if not nums1:
        if not nums2:
            raise ValueError('Input arrays cannot be both empty')
        else:
            return median(nums2)
    """handle cases with empty lists"""

    max_element = max(nums1[-1], nums2[-1])
    min_element = min(nums1[0], nums2[0])

    A = MyList(min_element, max_element, nums1)
    B = MyList(min_element, max_element, nums2)
    """these are special types of list adapted for this task"""
    future_median_index = (len(A) + len(B)) // 2

    low, high = 0, len(A) - 1
    """prepare indexes for binary search"""

    """perform binary search on num1"""
    while high >= low:
        i = (low + high) // 2
        j = future_median_index - i - 1
        if A[i] > B[j]:
            high = i - 1
        else:
            low = i + 1

    """Select elements that are in the middle and potentially could be median"""
    if (len(A) + len(B)) % 2:
        candidates = []
        if A[i] >= B[j]:
            candidates.append(B[j+1])
            candidates.append(A[i])
            candidates.append(max(A[i-1], B[j]))
        else:
            candidates.append(A[i+1])
            candidates.append(B[j])
            candidates.append(max(A[i], B[j-1]))
    else:
        candidates = [A[i], B[j]]
        if A[i] >= B[j]:
            candidates.append(A[i-1])
            candidates.append(B[j+1])
        else:
            candidates.append(B[j-1])
            candidates.append(A[i+1])

    candidates.sort()
    """median element(s) of the composed list are the actual median of the merged array"""
    return median(candidates)


class MyList(UserList):
    def __init__(self, min_el, max_el, array=None):
        """Special list class, adapted to the solution of this task

        Args:
            min_el: minimal value that shall be return for index < 0
            max_el: minimal value that shall be return for index > len(self) - 1
            array: list which is the data of this class
        """
        super().__init__(array)
        self._min = min_el
        self._max = max_el

    def __getitem__(self, index):
        if index > len(self) - 1:
            return self._max
        if index < 0:
            return self._min
        else:
            return super().__getitem__(index)


def median(array: list) -> float:
    """Get median value of the sorted list"""
    if len(array) == 0 or array is None:
        raise ValueError('Expected numeric list with at least 1 element')
    mid_index = len(array) // 2
    if len(array) % 2:
        return float(array[mid_index])
    else:
        return (array[mid_index] + array[mid_index - 1]) / 2
