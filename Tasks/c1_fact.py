def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n == 0:
        return 1
    return factorial_recursive(n - 1) * n



def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    n, b = 1, 1
    for i in range(n):
        yield n
        n, b = b, n + b
    d = factorial_iterative(n)
    print(d)
