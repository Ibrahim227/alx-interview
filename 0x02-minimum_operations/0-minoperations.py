#!/usr/bin/python3
"""Import required module/lib"""


def minOperations(n) -> int:
    """
        write a method that calculates the fewest number
        of operations needed to result in exactly n H characters in the file
    Returns: integer
    """
    str = 'H'
    op = 0
    fa = 2

    if n < 0:
        return 0
    while n > 1:
        while n % fa == 0:
            n //= fa
        fa += 1
    return op
