#!/usr/bin/env python3
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""
N = '''75
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
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''.split('\n')

# N = '''3
# 7 4
# 2 4 6
# 8 5 9 3'''.split('\n')
from locale import currency
import sys

if __name__ == "__main__":

    class Node():

        def __init__(self, data):
            self.data = int(data)
            self.left = None
            self.right = None

        def __repr__(self):
            return str(self.data)

    def build_tree(triangle):
        '''My custom algo to build a tree representation from the triangle string provided.
        At first, I thought normal binary tree was needed, but this problem has overlapping nodes.
        '''
        # Init the root node.
        root = Node(triangle[0][0])
        # Get length of trianlge to control our main iterator.
        num_rows = len(triangle)
        # Create a list to hold the current 'leaf' nodes we want to add another row of leaves to.
        leaf_nodes = [root]

        for row in range(1, num_rows):
            # Child row will be the next leaf nodes to add
            child_row = triangle[row]
            # Empty list to hold the new leaf Node objects we're about to add
            new_leaf_nodes = []
            # Keep track of those pesky inner, overlapping nodes.
            # ALL nodes to add are:
            #   left: new
            #   right: overlapping most of the time, or new
            overlapping_node = None
            # Add new leaves to each leaf we currently have
            for i, leaf in enumerate(leaf_nodes):
                # The overlapping_node exists if it was previously added as the
                # right leaf to some node. Thus it is the next leaf's 'left' child.
                if overlapping_node:
                    leaf.left = overlapping_node
                else:
                    # This only happens when i == 0. So legit create a new node and record it.
                    leaf.left = Node(child_row[i])
                    new_leaf_nodes.append(leaf.left)
                # Always make the right node.
                leaf.right = Node(child_row[i + 1])
                # Update new overlapping node.
                overlapping_node = leaf.right
                # Always record right leaf nodes
                new_leaf_nodes.append(leaf.right)
            # Next iteration will use the new leaves we just added.
            leaf_nodes = new_leaf_nodes

        return root

    N = [n.split() for n in N]
    # print(N)
    tree_root = build_tree(N)
    max_sum = 0

    def calucate_max_sum(node, curr_sum):
        '''Recursively find max sum out of all paths.'''
        # Global state to hold max sum we've seen so far
        global max_sum

        # Hit end of tree, so return
        if node == None:
            return

        # Update sum to hold sum of all nodes on path from root to this node.
        curr_sum += node.data

        # Update max sum once leaf is hit
        if node.left == None or node.right == None:
            max_sum = max(max_sum, curr_sum)

        # Keep on recurrin'
        calucate_max_sum(node.left, curr_sum)
        calucate_max_sum(node.right, curr_sum)

    calucate_max_sum(tree_root, 0)
    print(f"The path with the greatest sum gives a sum of: {max_sum}")
