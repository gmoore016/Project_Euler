"""
Gideon Moore

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import math


def main(n):
    """
    Finds the largest prime factor of n
    """

    # From the fundamental theorem of arithmetic, we know that
    # n = sum_i(prime_i^(k_i)). This means if we just repeatedly
    # divide by the smallest possible prime factor, the final value
    # must be the largest possible prime factor

    # Note this solution therefore requires a list of all possible
    # prime factors of n. We know that there exists an upper bound of
    # sqrt(n) on factors of n. Given an upper bound, we can apply
    # a standard prime number sieve to generate a list of primes
    prime_list = gen_possible_factors(n)

    # For each possible factor of n
    for prime in prime_list:

        # Divide it out evenly as many times as possible
        while not n % prime:
            # We will want to replace n with the "de-primed" value
            new_val = n // prime

            # However, if the value after de-priming is 1, that
            # was the largest prime factor
            if new_val == 1:
                return prime

            # Otherwise, just replace the value
            n = new_val

    # If, after factoring out all primes up to sqrt(n), the value is not 1,
    # then the remaining value must be prime
    return n


def gen_possible_factors(n):
    """
    Given an integer n, generates all possible prime factors using a
    prime number sieve and the fact that all factors of n <= sqrt(n)
    """

    # We only care about integer factors up to sqrt(n), so calculate
    # our bound
    bound = math.floor(math.sqrt(n))

    # Generates a list such that could_be_prime[i] is true so long as i
    # could still be prime. We only care about factors <= sqrt(n), so
    # the array stops there.
    #
    # Note we're marking 0 and 1 as "could be prime," but we never access
    # those values so it doesn't matter
    could_be_prime = [True] * (bound + 1)

    # List of confirmed primes returned by function
    confirmed_primes = []

    # Start at 2, the first prime number, and continue until reaching the bound
    for i in range(2, bound + 1):
        # If we reach a number, and it can still be prime...
        if could_be_prime[i]:
            # ...it is confirmed prime, so we add it to the list.
            confirmed_primes.append(i)

            # From there, we knock out all multiples below the bound as "not prime"
            j = 2 * i
            while j < bound:
                could_be_prime[j] = False
                j = j + i

    # After completing this for all values below the bound, we have our list of primes!
    return confirmed_primes

print(main(600851475143))

