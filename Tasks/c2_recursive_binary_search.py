from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, first_el=0, last_el=None) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if last_el is None:
        last_el = len(arr) - 1

    if last_el < first_el:
        return None
    mid = (first_el + last_el) // 2

    if arr[mid] == elem:
        return mid
    elif elem > arr[mid]:
        return binary_search(elem, arr, mid+1, last_el)
    elif elem < arr[mid]:
        return binary_search(elem, arr, first_el, mid-1)







