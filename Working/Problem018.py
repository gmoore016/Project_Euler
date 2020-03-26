"""
Gideon Moore

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

TREE_STRING = "75\n95 64\n17 47 82\n18 35 87 10\n20 04 82 47 65\n19 01 23 75 03 34\n88 02 77 73 07 63 67\n99 65 04 28 06 16 70 92\n41 41 26 56 83 40 80 70 33\n41 48 72 33 47 32 37 16 94 29\n53 71 44 65 25 43 91 52 97 51 14\n70 11 33 28 77 73 17 78 39 68 17 57\n91 71 52 38 17 14 91 43 58 50 27 29 48\n63 66 04 68 89 53 67 30 73 16 69 87 40 31\n04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"


class Triangle:
    def __init__(self, tri_str):
        # Creates a list of strings representing each row
        tri_lines = tri_str.split("\n")

        # Generates first "leaf" array from bottom string in triangle
        leaf_array = [Node(int(j)) for j in tri_lines[-1].split(' ')]

        # Make our way up the triangle, pointing parents to children
        for i in range(2, len(tri_lines) + 1):
            # Generates array of parent nodes
            parent_array = [Node(int(j)) for j in tri_lines[-i].split(' ')]

            # For each parent node, assign the appropriate left and
            # right child nodes
            for j in range(len(parent_array)):
                parent_array[j].set_left(leaf_array[j])
                parent_array[j].set_right(leaf_array[j + 1])

            # Move up the tree, setting the new parents to be leaves
            leaf_array = parent_array

        # Set the root of the triangle to be the top number
        self.root = leaf_array[0]

    def find_best_path(self):
        """Finds the highest value path from the root to the base"""
        return self.root.find_best_path()

    def get_root(self):
        return self.root


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.cache = None

    def find_best_path(self):
        """
        Method for finding the value of the greatest path to the
        bottom of the triangle
        """

        # If we haven't already cached the solution
        if not self.cache:
            # If we're at a leaf, set the cache to the node value
            if not self.left or not self.right:
                self.cache = self.value

            # If we're at a parent, get the best path of each leaf,
            # choose that value, then add the parent's node value
            # and cache the solution
            else:
                left_path = self.left.find_best_path()
                right_path = self.right.find_best_path()

                self.cache = max(left_path, right_path) + self.value

        return self.cache

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_value(self):
        return self.value

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


def main():
    """Function to find the maximal sum from top to bottom of the above triangle"""

    # Converts string to array representation of a binary tree
    # Needed to add None as first index for nice properties; will not be used
    # With this method, we can access an element's children by doubling its index; the left
    # child is at index 2i while the right child is at 2i + 1
    triangle = Triangle(TREE_STRING)

    solution = triangle.find_best_path()

    print(solution)
    return solution


def find_max_sum(root, tree, cache):
    """
    Given a tree stored as an array and a starting root element,
    this function returns the maximum possible sum to the bottom
    starting with the root element. Uses cache for dynamic
    programming speedup
    """
    # If the root in question hasn't been solved yet
    if cache[root] < 0:
        root_val = tree[root]
        left_branch = root_val + find_max_sum(2 * root, tree, cache)
        right_branch = root_val + find_max_sum(2 * root + 1, tree, cache)

        cache[root] = max(left_branch, right_branch)

    return cache[root]


main()
