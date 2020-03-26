"""
Gideon Moore

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""


def main(n):
    """
    Returns the nth prime number
    """
    # Seed the first two prime numbers
    # By starting with both 2 and 3, we can check only odd primes
    primes = [2, 3]
    num_primes = 2

    # This is the first number to test
    value = 5

    # Continue until we reach the desired prime
    while num_primes < n:
        # If the number is prime, add it to the list and increase the count
        if is_prime(value, primes):
            primes.append(value)
            num_primes = num_primes + 1

        # Check the next odd number
        value = value + 2

    # Return the last found prime
    return primes[-1]


def is_prime(value, primes):
    """
    When provided with a value and a list of known prime numbers
    less than that value, tests whether that value is prime
    """

    # We're skipping evens, so no need to test 2, the first prime
    i = 1

    # So long as the prime is less than the square root of the value, there could still exist a prime factor
    while primes[i] * primes[i] <= value:

        # If the value ever divides evenly, we know it is not prime
        if not value % primes[i]:
            return False

        # Check the next known prime
        i = i + 1

    # If none of the known primes work, the newest value must also be prime
    return True


print(main(10001))

