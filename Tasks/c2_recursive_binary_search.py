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


    if first_el >= last_el:
        return None

    if arr[first_el] == elem:
        return first_el
    if arr[last_el] == elem:
        return last_el

    while first_el < last_el:
        mid = (first_el + last_el) // 2
        # elem_found = arr[mid]

        if arr[mid] == elem:
            return mid
        if arr[mid] < elem:
            last_el = mid + 1
        else:
            first_el = mid - 1
        if arr[mid] != elem:
            break
    return None


        #     return binary_search(mid - 1, elem_found)
        # else:
        #     return binary_search(mid + 1, elem_found)

if __name__ == '__main__':
    print(binary_search(3, arr=[7, 4, 3, 123]))







