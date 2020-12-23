"""
My little Stack
"""
from typing import Any
my_list_stack = [5, 6, 7]
print(my_list_stack)

def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    # Операция добавления элемента на стек называется «push», удаления — «pop». Последний добавленный элемент называется верхушкой
    # стека, или «top», и его можно посмотреть с помощью операции «peek»


    # my_list_stack.append(6)
    # my_list_stack.append(7)
    # my_list_stack.append(5)
    my_list_stack.append(elem)
    print(my_list_stack)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    my_list_stack.pop()
    print(my_list_stack)
    return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    my_list_stack.insert(2, -1)
    print(ind)
    return None


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    return None
if __name__ == '__main__':
    push(52)
    pop()
    pop()
    peek()

