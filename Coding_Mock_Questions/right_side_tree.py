'''
Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

            1
    2               3
4        5     6        7
    9  

Right View = [1, 3, 7, 9]
'''

# TC: O(n) SC: O(n) - Skewed Tree in worst case or else can store O(logn) for each level

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def rightView(root):
    if root is None:
        return []
    
    result = []

    queue = deque()
    queue.append(root)

    while len(queue):
        size = len(queue)

        node = None # This will have the right node for each level at the end of each level's iteration

        while size > 0:
            node = queue.popleft()

            if node.left is not None:
                queue.append(node.left)
            
            if node.right is not None:
                queue.append(node.right)

            size -= 1

        result.append(node.val)

    return result

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(9)

root.right = Node(3)
root.left.right = Node(6)
root.right.right = Node(7)

print(rightView(root))