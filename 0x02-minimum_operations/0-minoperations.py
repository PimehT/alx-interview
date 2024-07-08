#!/usr/bin/python3
"""
find the minimum operations to have `n` characters in a text editor
when the text editor can only execute two commands: `Copy All` and
`Paste`
"""


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return factors


def minOperations(n):
    if n < 2:
        return 0
    elif len(prime_factors(n)) == 1:
        return n
    else:
        return sum(prime_factors(n))
