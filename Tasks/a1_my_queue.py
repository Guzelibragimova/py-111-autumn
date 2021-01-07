"""
My little Queue
"""
from typing import Any
my_list_queue = [5, 8, 4]  # слева конец очереди, справа начало


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """

    my_list_queue.insert(0, elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """

    return my_list_queue.pop() if my_list_queue else None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if ind >= len(my_list_queue):
        return None
    return my_list_queue[-1 - ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    my_list_queue.clear()
    return None
