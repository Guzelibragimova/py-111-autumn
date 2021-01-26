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

    min_el = arr[0]  # самый первый элемент берем и считаем его минимальным
    count = 0
    for i in range(len(arr)):
        if arr[i] < min_el:
            min_el = arr[i]
            count = i
    return count
