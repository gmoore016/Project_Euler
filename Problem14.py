"""
Gideon Moore

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def main(bound):
    """
    Given an upper boundary, this function returns the number <= the bound which
    produces the longest Collatz chain
    """

    # Need to track the max chain length and the input which yields the max chain
    max_len = 0
    max_input = 0

    # Initializes our cache
    cache = dict()
    # We define 1 to have a Collatz chain length of 1
    cache[1] = 1

    # Test for each number
    for i in range(1, bound):
        # Find the chain length
        chain_length = find_chain_length(i, cache)

        # If it's greater than the existing maximum, save and continue
        if chain_length > max_len:
            max_input = i
            max_len = chain_length

    # Return the number beneath the bound with the longest Collatz chain
    return max_input


def find_chain_length(num, cache):
    """
    Function to find the length of a Collatz chain starting at num.

    Function checks whether the chain length of num is already present in the cache. If so, returns.
    Otherwise, performs a recursive call on the collatz number of num, and adds one to mark the extra
    step in the chain. Upon return of the recursive call, saves the result to the cache then returns.
    """
    if num not in cache:
        cache[num] = find_chain_length(collatz(num), cache) + 1

    return cache[num]


def collatz(num):
    """
    Given a number, returns the next number in the Collatz sequence
    """

    # If the number is odd
    if num & 1:
        collatz_val = 3 * num + 1

    # If the number is even
    else:
        collatz_val = num // 2

    return collatz_val


print(main(1000000))

