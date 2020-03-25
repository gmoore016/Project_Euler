"""
Gideon Moore

Having three black objects B and one white object W they can be grouped in 7 ways like this:
(BBBW)	(B,BBW)	(B,B,BW)	(B,B,B,W) 	(B,BB,W)	(BBB,W)	(BB,BW)
In how many ways can sixty black objects B and forty white objects W be thus grouped?
"""


def main(black, white):
    # Cache to store number of possible groupings given x black objects
    # and y white objects
    cache = [[-1 for x in range(black)] for y in range(white)]

    result = find_groupings(black, white, cache)

    return result


def find_groupings(black, white, cache):
    # If we haven't cached this result yet
    if cache[black][white] < 0:

        # Do the hard part

        # Note the problem is symmetrical, since there are equal
        # ways to group x white balls and y black balls compared to
        # y white balls and x black balls
        # Therefore if possible we should equalize results
        # in the cache across the diagonal
        if white < len(cache) and black < len(cache[0]):
            cache[white][black] = result

        if black < len(cache) and white < len(cache[0]):
            cache[black][white] = result

        return result

    # Dynamic programming y'all
    else:
        return cache[black][white]