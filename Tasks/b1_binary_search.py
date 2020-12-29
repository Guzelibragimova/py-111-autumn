from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    local_arr = arr[:]
    left_border = 0
    right_border = len(local_arr) - 1

    while local_arr:
        if local_arr[left_border] == elem:
            return left_border
        elif local_arr[right_border] == elem:
            return right_border
        middle = left_border + (right_border - left_border) // 2
        if local_arr[middle] == elem:
            return middle
        elif local_arr[middle] < elem:
            left_border = middle + 1
        elif local_arr[middle] > elem:
            right_border = middle - 1
        if left_border >= right_border:
            break

    return None
