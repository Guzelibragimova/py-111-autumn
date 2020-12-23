"""
My little Stack
"""
from typing import Any

my_list_stack = [5, 6, 7] #вершина справа


def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    # Операция добавления элемента на стек называется «push», удаления — «pop». Последний добавленный элемент называется верхушкой
    # стека, или «top», и его можно посмотреть с помощью операции «peek»
    # запушить значит на верх добавить, справа как append


    my_list_stack.append(elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    if not my_list_stack:
        return None
#pop принимает индекс и можно удалить любой элемент не только последний
    return my_list_stack.pop()



def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    #insert добавляет на место индекса(с 0,1,2) в списке
    # index позволяет узнать индекс или позицию элемента в последовательности
    #a = my_list_stack.index(ind)

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
if __name__ == '__main__':
    print(my_list_stack)
    push(52)
    # print(my_list_stack)

    # pop()
    # pop()
    push(47)
    # peek(6)
    # clear()
    # print(my_list_stack)
    # push(4)
    # print(my_list_stack)
    #
    # print(pop())
    # print(my_list_stack)
    # print(pop())

    print(peek(0))
    print(peek(1))
    print(peek(2))


