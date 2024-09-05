#!/usr/bin/python3
"""the prime game"""


def sieve_of_eratosthenes(max_n):
    """ Returns a list of prime numbers up to max_n using the Sieve of Eratosthenes. """
    is_prime = [True] * (max_n + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False
    return is_prime


def isWinner(x, nums):
    '''
    x: int
    nums: int
    '''
    if x <= 0 or not nums:
        return None

    max_n = max(nums)

    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = sum(primes[1:n+1])

        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
