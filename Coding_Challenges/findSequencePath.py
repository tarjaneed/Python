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

def matchSequence(root, sequence):
    if root is None:
        return False
    
    temp_seq.append(root.data)

    if not root.left and not root.right:
        # Match and return result of temp_seq and input seq
        temp_seq = ''.join(str(x) for x in temp_seq)
        sequence = ''.join(str(x) for x in sequence)

        print(temp_seq)
        print(sequence)

        return temp_seq == sequence

    return matchSequence(root.left, sequence) or matchSequence(root.right, sequence)

root = Node(1)
root.left = Node(0)
root.left.left = Node(1)

root.right = Node(1)
root.right.left = Node(6)
root.right.right = Node(5)

print(matchSequence(root, [1, 1, 6]))
