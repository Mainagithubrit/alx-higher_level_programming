#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers.

"""


def find_peak(list_of_integers):
    """finds peak in an unsorted list

    Args:
        List_of_integers: A list of integers(unsorted)
    Returns:
        Peak: The peak value found on the list.
    """
    if list_of_integers == []:
        return None
    length = len(list_of_integers)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if (list_of_integers[mid] > list_of_integers[mid - 1] and
                list_of_integers[mid] > list_of_integers[mid + 1]):
            return list_of_integers[mid]
        if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_of_integers[start]
