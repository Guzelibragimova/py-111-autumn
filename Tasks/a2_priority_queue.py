"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
from collections import deque
my_priority_queue = deque()


def enqueue(elem: Any, priority: int = 0) -> None:
    """cv
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    my_priority_queue.insert(0, elem)
    return None


if __name__ == '__main__':
    enqueue(5)

def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    return  my_priority_queue.pop() if my_priority_queue else None



def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """

    if ind >= len(my_priority_queue):
        return None
    return my_priority_queue[-1 - ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    my_priority_queue.clear()
    return None


