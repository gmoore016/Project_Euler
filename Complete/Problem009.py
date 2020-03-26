"""
Gideon Moore

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def main():

    # Solutions are defined by pairs of a and b since the pair
    # defines only one possible value for c

    # a is defined to be less than b
    # Given a < b < c, a < 333; if a = 333, b + c = 667
    # If this is so, c >= 334 as c > b, but this means b <= 333
    # This implies b == a, which is a contradiction. Thus, a < 333.
    #
    # Further, a is a natural number, so a >= 1
    for a in range(1, 333):
        # As b is greater than a, we can start with a + 1
        #
        # Further, as b < c, we know b < 1000 - 2a
        # This is because a + b + c = 1000 -> b = 1000 - a - c
        #  -> b < 1000 - 2a since a < c
        for b in range(a + 1, 1000 - 2 * a):
            # An (a, b) pair allow only one possible c
            c = 1000 - a - b

            # If a2 + b2 = c2, then we're done!
            if a * a + b * b == c * c:
                # Find product as desired by prompt
                product = a * b * c

                print(a, b, c)
                print(product)
                return product


main()
