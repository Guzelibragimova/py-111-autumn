"""
My little Queue
"""
from typing import Any

#сделали очередь списком
my_queue = [] #слева конец очереди, справа начало

def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    my_queue.insert(0, elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    my_queue.pop() if my_queue else None
    return None
#берет элемент с начала и возвращает

def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    return my_queue[len(my_queue)-1]

#посмотреть элемент но его не вытаскивает, где начало очереди оттуда идем

def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    return None
