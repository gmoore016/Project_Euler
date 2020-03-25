"""
Gideon Moore

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""


def main(n):
    """
    Returns the nth prime number
    """

    primes = [2, 3]
    num_primes = 2

    value = 5

    while num_primes < n:
        if is_prime(value, primes):
            primes.append(value)
            num_primes = num_primes + 1

        value = value + 2

    return primes[-1]


def is_prime(value, primes):
    """
    When provided with a value and a list of known prime numbers
    less than that value, tests whether that value is prime
    """
    # We're skipping evens, so no need to test 2
    i = 1
    while primes[i] * primes[i] <= value:
        if not value % primes[i]:
            return False
        i = i + 1

    return True


print(main(10001))

