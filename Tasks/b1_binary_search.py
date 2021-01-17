from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    first_el = 0
    last_el = len(arr) - 1

    if arr[last_el] == elem:
        return last_el
    if arr[first_el] == elem:
        return first_el
    if first_el > last_el:
        return None
    while first_el <= last_el:
        mid = (first_el + last_el) // 2
        elem_found = arr[mid]
        if elem_found == elem:
            return mid
        if elem_found > elem:
            last_el = mid - 1
        else:
            first_el = mid + 1
    return None


    # print(elem, arr)
    # return None

