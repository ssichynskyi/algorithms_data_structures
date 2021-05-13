def solution(array: [int]) -> int:
    """Find smallest positive integer not in array

    Args:
        array: array of ints

    Returns:
        the smallest positive int not in input array

    """
    all_uniques = set(array)

    try:
        max_array_el = max(0, max(all_uniques))
    except ValueError:
        # handle case of empty array
        max_array_el = 0
    # max integer cannot be bigger than either maximal positive element of the array
    # or length of the unique values:
    max_int = min(len(all_uniques), max_array_el)
    for i in range(1, max_int + 1):
        # 'in' operation for 'set' has average O(1) time complexity
        if i not in all_uniques:
            return i
    return max_int + 1
