import math

def arccos_series(x, eps):
    """
    Calculate arccos(x) using power series expansion.
    Max iterations: 500
    """
    if abs(x) > 1:
        raise ValueError("x must be in range [-1, 1]")

    result = math.pi / 2
    term = x
    n = 0
    sign = -1

    while abs(term) > eps and n < 500:
        result += sign * term
        n += 1
        term = (math.factorial(2 * n) /
                (4**n * (math.factorial(n))**2 * (2 * n + 1))) * x**(2 * n + 1)
        sign = -1

    return result, n, math.acos(x)
