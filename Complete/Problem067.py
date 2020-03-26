"""
Gideon Moore

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

(Note this is almost identical to problem 18, but now at a much larger scale and taking input from a file)
"""

class Triangle:
    def __init__(self, input_file):

        # Creates a list of strings representing each row
        triangle_file = open(input_file)
        tri_lines = triangle_file.readlines()
        triangle_file.close()

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


class Node:
    """
    Class representing a single point in the triangle
    Each node contains a value, equal to its number, as well as a left child and right child
    which link to the two nodes accessible from the given node.
    Lastly, each node caches the value of its highest value path once it is found once.
    """
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

        # Return the cached solution
        return self.cache

    # Setters for the two child nodes
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
    triangle = Triangle("../Inputs/input067.txt")

    # Finds the optimal path from the root to the base
    solution = triangle.find_best_path()

    print(solution)
    return solution


main()
