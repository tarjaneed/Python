'''
Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. 
The diameter of a tree may or may not pass through the root.

            1
    2               3
        4       5       6

Output: 5 i.e. [4, 2, 1, 3, 6]
'''

# TC: O(n) SC: O(h)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def depth(root):
    global diameter
    if root is None:
        return 0
    
    left_depth = depth(root.left)
    right_depth = depth(root.right)

    current_diameter = 1 + (left_depth + right_depth)
    diameter = max(diameter, current_diameter)

    return 1 + max(left_depth, right_depth) # Depth of a node is the maximum depth of left or right subtree

def findDiamter(root):
    global diameter
    diameter = 0
    depth(root)
    return diameter

root = Node(1)
root.left = Node(2)
root.left.right = Node(4)

root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(6)

print(findDiamter(root))