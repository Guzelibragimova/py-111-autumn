"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """

    min_el = arr[0]
    for i in arr:
        if i < min_el:
            min_el = i

    return min_el
    # return -1
