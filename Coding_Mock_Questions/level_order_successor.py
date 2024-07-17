'''
Given a binary tree and a node, find the level order successor of the given node in the tree. 
The level order successor is the node that appears right after the given node in the level order traversal.
            1
    2               3
4        5     6        7
    9  

Give node = 3
Level Order Successor = 4
'''

# TC: O(n) SC: O(n) - Skewed Tree in worst case or else can store O(logn) for each level

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findLevelOrderSuccessor(root, key):
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        node = queue.popleft()

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

        if node.val == key:
            break

    if queue:
        return queue.popleft().val

    return None

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(9)

root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

print(findLevelOrderSuccessor(root, 3)) # 4
print(findLevelOrderSuccessor(root, 5)) # 6
print(findLevelOrderSuccessor(root, 7)) # 9