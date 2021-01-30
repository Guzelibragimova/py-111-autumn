"""
My little Stack
"""
from typing import Any

my_list_stack = [5, 6, 7]


def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """

    my_list_stack.append(elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    if not my_list_stack:
        return None

    return my_list_stack.pop()


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """

    print(ind)
    if ind >= len(my_list_stack):
        return None
    return my_list_stack[-1 - ind]


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    my_list_stack.clear()
    return None
