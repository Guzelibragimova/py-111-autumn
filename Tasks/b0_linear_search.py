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
    min_el = arr[0] # самый первый элемент берем и считаем его минимальным
    for i in arr:
        if arr[i] < min_el:
            min_el = arr[i]
            return i
        if arr[i] < 0:
            min_el = arr[i]
            return i
        print(i)
    return min_el

if __name__ == '__main__':
    my_list = [9]
    print(min_search(my_list))