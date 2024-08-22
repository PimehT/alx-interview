#!/usr/bin/python3
"""
Given an amount of money, write a function to compute
the minimum number of coins needed to make up that amount.
If that amount of money cannot be made up by any combination
of the coins, return -1.
"""


def makeChange(coins, total):
    """
    Given an amount of money, write a function to compute
    the minimum number of coins needed to make up that amount.
    If that amount of money cannot be made up by any combination
    of the coins, return -1.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    n = len(coins)
    result = 0
    i = 0
    while i < n and total > 0:
        result += total // coins[i]
        total = total % coins[i]
        i += 1
    if total == 0:
        return result
    return -1
