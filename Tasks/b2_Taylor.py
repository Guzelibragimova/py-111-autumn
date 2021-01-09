"""
Taylor series
"""
from typing import Union
from itertools import count
from math import factorial


DELTA = 0.0001


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    def item(n):
        # n каждый раз новое по этой формуле считаем
        return (x ** n)/factorial(n)

    sum_ = 0
    for i in count():
        current_value = item(i)
        sum_ += current_value

        if abs(current_value) <= DELTA:
            return sum_


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    def item(n):
        # n каждый раз новое по этой формуле считаем
        return (pow(-1, n)) * (pow(x, 2 * n + 1))/(factorial(2 * n + 1))

    sum_ = 0
    for i in count():
        current_value = item(i)
        sum_ += current_value

        if abs(current_value) <= DELTA:
            return sum_
