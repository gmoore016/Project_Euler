"""
Gideon Moore

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of a or b below some input n.
"""


def main(a, b, n):
    # Note that when counting by a, you get the arithmetic sequence
    # a + 2a + 3a ... so long as ka <= n. This is equal to
    # a * sum(1, floor(n / a)).
    #
    # We need to subtract 1 from n before taking floor because
    # we only care about numbers less than n. If it were less
    # than or equal to, we would use n proper.

    a_sum = sum_one_to_n((n - 1) // a) * a
    b_sum = sum_one_to_n((n - 1) // b) * b

    # If we simply sum a_sum and b_sum, we will double count
    # all factors which are multiples of both a and b. Thus,
    # we need to subtract off the sum of all multiples of
    # both a and b to get the correct solution
    prod = a * b
    intersection_sum = sum_one_to_n((n - 1) // prod) * prod

    result = a_sum + b_sum - intersection_sum
    print(result)
    return result


def sum_one_to_n(n):
    """
    Simple function which, when given a natural number n,
    returns the sum of all numbers from 1 <= i <= n

    based on fact sum from 1 to n = n * (n + 1) / 2
    """

    # Since either n or n + 1 is always even, this will always
    # be an integer. Therefore, use integer division for speed
    # and to return an int
    return n * (n + 1) // 2


main(3, 5, 1000)
