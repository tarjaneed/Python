'''
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

Example 1: Sequence: [1, 1, 6]
  Output: True
Example 2: Sequence: [1, 0, 8]
  Output: False

- DFS
- Start from the root
- We stop at leaf node -> no left and right child

- root
- left subtree check the path save it and match with the given sequence
- right subtree check the path return

TC : O(n)
SC: O(n)
'''

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def matchSequence2(root, givenSequence, pathSequence=[]):
    if root is None:
       return pathSequence == givenSequence

    newPathSequence = pathSequence + [root.data]
    return matchSequence2(root.left, givenSequence, newPathSequence) or matchSequence2(root.right, givenSequence, newPathSequence)

root = Node(1)
root.left = Node(0)
root.left.left = Node(1)

root.right = Node(1)
root.right.left = Node(6)
root.right.right = Node(5)

print(matchSequence2(root, [1, 0, 1]))
print(matchSequence2(root, [1, 1, 6]))
print(matchSequence2(root, [1, 0, 8]))