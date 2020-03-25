"""
Gideon Moore

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""


def main(side_len):
    # Creates a matrix which stores how many routes exist from point (i, j)
    # Need side_len + 1 since there is a point at distance 0
    cache = [[-1 for x in range(side_len + 1)] for y in range(side_len + 1)]
    cache[side_len][side_len] = 1

    # We're looking for the number of routes from the top-left point, (0,0)
    result = get_dist(0, 0, side_len, cache)

    # Get the total number of paths from the top left to the bottom right
    return result


def get_dist(i, j, side_len, cache):
    """
    When starting at point (i, j), returns how many routes exist to point (side_len, side_len)
    """
    # If the answer is not currently cached
    if cache[i][j] < 0:
        # If we can move right, calculate the paths available from the right point
        # If we cannot move right, that provides 0 options
        if i < side_len:
            right_options = get_dist(i + 1, j, side_len, cache)
        else:
            right_options = 0

        # Same as above, but for downward moves
        if j < side_len:
            down_options = get_dist(i, j + 1, side_len, cache)
        else:
            down_options = 0

        # Our total choices are those available moving right plus those
        # available moving down
        total_options = right_options + down_options

        # Store the result once found
        cache[i][j] = total_options

    # Store our previously calculated value
    return cache[i][j]


print(main(20))
