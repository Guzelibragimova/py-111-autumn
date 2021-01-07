"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
from collections import deque
my_priority_queue = []


def enqueue(elem: Any, priority: int = 0) -> None:
    """cv
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    a = [i for i in range(elem)]
    for i in a:
        my_priority_queue.insert(0, i)
    sorted_ = []
    for j in a:
        sorted_.append(my_priority_queue.pop())
    print(a, sorted_)


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    return None


if __name__ == '__main__':
    enqueue(10)