from typing import List


def sort_(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) == 1:
        return container
    else:
        middle = len(container) // 2
        left = sort_(container[:middle])
        right = sort_(container[middle:])
        return merge1(left, right)


def merge1(left_container: List[int], right_container: List[int]) -> List[int]:
    current_elem_from_left_container = 0  # текущий элемент из левого контейнера
    current_elem_from_right_container = 0  # текущий элемент из правого контейнера
    merged_container = []

    for _ in range(len(left_container) + len(right_container)):
        if left_container[current_elem_from_left_container] <= right_container[current_elem_from_right_container]:
            merged_container.append(left_container[current_elem_from_left_container])
            current_elem_from_left_container += 1
        else:
            merged_container.append(right_container[current_elem_from_right_container])
            current_elem_from_right_container += 1
        while current_elem_from_left_container < len(left_container)+1:
            merged_container.append(left_container)
            current_elem_from_left_container += 1
            break
        while current_elem_from_right_container < len(right_container)+1:
            merged_container.append(right_container)
            current_elem_from_right_container += 1
            break

        return merged_container

        if len(container) < 2:
            return container

            middle = len(container) // 2
            return merge1(sort(container[:middle]), sort(container[middle:]))



