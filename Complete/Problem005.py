"""
Gideon Moore

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

(Note:  I think the dynamic programming here is likely overkill for an input of only 20 continuous factors.
        However, I'm relatively confident my version scales significantly better to higher inputs. Have tested
        up to 150 and compute time is completely unnoticeable.)
"""


def main(continuous_factors):
    """
    Finds the smallest number that is divisible by all numbers from 1 to continuous_factors
    """

    # The goal of this function is to find the least common multiple of the first continuous_factors natural numbers
    #
    # We know by applying the fundamental theorem of arithmetic that the least common multiple of a set of numbers
    # is the product of all prime factors present in the set, raised to the maximal power present in the set.
    # For example, 4 = 2^2 and 6 = 2 * 3, so the LCM of 4 and 6 is 2^2 * 3 = 12.
    #
    # Therefore, all we need to do is reduce each element to its prime factors, then take the max number of
    # occurrences for each

    # Dictionary to store dictionaries linking numbers to the magnitudes of their prime factors
    cache = dict()

    # List of primes less than or equal to continuous_factors to aid in factorization
    primes = gen_possible_factors(continuous_factors)

    # Max detected magnitude of each factor
    # To start with, all magnitudes are zero
    max_mags = dict()
    for prime in primes:
        max_mags[prime] = 0

    # Calculate factors for each number
    for number in range(1, continuous_factors + 1):
        # Dictionary linking number to its prime factors and magnitudes
        prime_magnitudes = get_magnitudes(number, primes, cache)

        # For each prime, see if the factor's magnitude is the greatest so far
        # If so, save it
        for factor in primes:
            if prime_magnitudes[factor] > max_mags[factor]:
                max_mags[factor] = prime_magnitudes[factor]

    # Set value when all prime magnitudes are zero
    lcm = 1

    # For each prime...
    for prime in primes:
        # Multiply the value by the relevant prime a number of times equal to the maximum magnitude
        for i in range(max_mags[prime]):
            lcm = lcm * prime

    # Return the final product
    return lcm


def get_magnitudes(num, primes, cache):
    """
    Returns a dictionary of the form prime_factor:magnitude such that the product of prime_factor^magnitude over
    all elements of the dictionary equals num

    Primes is a dictionary of all primes possible in the problem

    Cache contains
    """

    # How 'bout that dynamic programming
    if num not in cache:
        # Dictionary linking factors to magnitudes
        mags = dict()

        # For each prime factor
        for prime in primes:

            # If the number divides it...
            if not num % prime:
                # Get the magnitude of the relevant prime in the quotient and add 1
                mag = 1 + get_magnitudes(num//prime, primes, cache)[prime]

            # Otherwise, the magnitude is 0
            else:
                mag = 0

            # Add that to the cache
            mags[prime] = mag

        # When the dict is done, cache it
        cache[num] = mags

    # Return the cached value
    return cache[num]


def gen_possible_factors(bound):
    """
    Generates a list of all primes <= bound
    """

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
            while j < bound + 1:
                could_be_prime[j] = False
                j = j + i

    # After completing this for all values below the bound, we have our list of primes!
    return confirmed_primes


print(main(20))













