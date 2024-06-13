'''
DFS on a Binary Tree - Preorder Traversal

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

Example:
Target Sum = 8. True -> Path 1 -> 2 -> 5

Target Sum = 20. False No Path matches the target

         1
    2          3
4       5   6     7    
'''

class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

# TC: O(n)
def DFSPreOrderTraversal(root):
    if root is None:
        return

    print(root.key, end=" ")
    DFSPreOrderTraversal(root.left)
    DFSPreOrderTraversal(root.right)

# TC: O(n) - worst we traverse all path / nodes and do not find matching sum SC: O(n) - unbalanced else O(h) -> height of the tree
def findTargetSum(root, targetSum):
    current_sum = 0
    return DFS_root_leaf(root, current_sum, targetSum)

def DFS_root_leaf(root, currentSum, targetSum):
    # Check if the given tree is empty
    if root is None:
        return False
    
    # Add the value of the node we are traversing to the sum
    currentSum += root.key

    # Now check if this node is leaf node or not i.e. it is leaf if it doesn't have left and right children
    # If it is leaf check current sum matches the target sum or not; if equal return True (Path Found) else False (This is not the Path)
    if root.left is None and root.right is None:
        return currentSum == targetSum
    
    # If this is not the leaf node; run DFS i.e. findTargetSum on left subtree first and then on the right subtree
    return DFS_root_leaf(root.left, currentSum, targetSum) or DFS_root_leaf(root.right, currentSum, targetSum)

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)

root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

DFSPreOrderTraversal(root)

print('\n')
print(findTargetSum(root, 8))
print(findTargetSum(root, 24))
print(findTargetSum(None, 24)) # Empty Tree