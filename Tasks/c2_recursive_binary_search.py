from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    first_el = 0
    last_el = len(arr) - 1
    mid = (first_el + last_el)//2
    if first_el >=  last_el:
        return None

    if arr[last_el] == elem:
        return last_el
    if arr[first_el] == elem:
        return first_el

    while first_el < last_el:
        elem_found = arr[mid]

        if elem_found != elem:
            return None
        if elem_found == elem:
            return mid
        if elem_found > elem:
            return binary_search(mid - 1, elem_found)
        else:
            return binary_search(mid + 1, elem_found)

if __name__ == '__main__':
    print(binary_search(300, arr=[7, 4, 3]))







