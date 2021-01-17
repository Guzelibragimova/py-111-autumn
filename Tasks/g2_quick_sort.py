from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    def _sort(left_border: int, right_border: int):
        if left_border == right_border:
            return
        selected_elem = container[left_border]
        left_border += 1
        # 6. Продолжаем уменьшать счетчики и менять элементы аналогичным образом, пока счетчики не встретятся – получаем индекс элемента,
        # левее которого все элементы меньше или равны опорному, а правее – больше опорного
        while left_border != right_border:
        # 3. Увеличиваем левый счетчик, пока он не встретит элемент больше или равный опорному
            while container[left_border] < selected_elem:
                left_border += 1
                return container
        # 4. Уменьшаем правый счетчик, пока он не встретит элемент меньше или равный опорному
            while container[right_border] > selected_elem:
                right_border -= 1

            # 5. Меняем элементы местами
            container[left_border], container[right_border] = container[right_border], container[left_border]

        _sort(left_border, selected_index)
        _sort(selected_index, right_border)

    return container

