'''
Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.
A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root. The path must contain at least one node.

        1
    2       3
4       5       6

Output: 16
The path with maximum sum is [4, 2, 1, 3, 6]

        1
    2       3

Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.


    -10
9           20
        15      7

Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
'''

'''
Approach:

We need to consider 3 cases:
1. We get the path below only so we do not go above to explore new nodes since we got our max answer i.e. the path starts from left goes to a node and converges to the right.
    path_found_below = root.val + left_sum + right_sum
2. We get good sum from left and right both. In this case we take maximum of left or right and add it to the root and allow it to explore ahead in search of finding the better sum.
    either_left_or_right = root.val + max(left_sum, right_sum)
3. We do not get any good sum from either left or right in this case, we just take root's val and allow it to explore above to check for the better sum.
    only_root = root.val

Also, keep updating the max_sum it would be max(max_sum, path_found_below, either_left_or_right, only_root) i.e. max of any 4 out of this.

Now, while returing we return max of Case 2 and Case 3 since we cannot return case since the path is already found and converged.
return max(either_left_or_right, only_root)
'''

# TC: O(n) - Traversing every node once SC: O(n) - Worst can be a tree is skewed

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def solve(root):
    global max_sum

    if root is None:
        return 0
    
    left = solve(root.left)
    right = solve(root.right)

    path_found_below = root.data + left + right
    either_left_or_right = root.data + max(left, right)
    only_root = root.data

    max_sum = max(max_sum, path_found_below, either_left_or_right, only_root)

    return max(either_left_or_right, only_root)

def findMaxSum(root):
    global max_sum
    max_sum = float('-inf')
    solve(root)
    return max_sum

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)

root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(6)
print(findMaxSum(root))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
print(findMaxSum(root))

root = Node(-10)
root.left = Node(9)

root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print(findMaxSum(root))

root = Node(-3)
print(findMaxSum(root))