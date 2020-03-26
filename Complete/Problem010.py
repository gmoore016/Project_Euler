"""
Gideon Moore

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def main(bound):
    """
    Calculates sum of all primes <= bound

    Note this is lifted almost wholesale from my solution to problem 5
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
    # Now we just take the sum
    prime_sum = sum(confirmed_primes)
    print(prime_sum)
    return prime_sum


main(2000000)
