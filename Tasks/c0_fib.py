def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n < 0:
        raise ValueError

    return fib_recursive(n - 1) + fib_recursive(n - 2)



def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


data = fib_iterative(10)
print(data)


