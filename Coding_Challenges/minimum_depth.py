'''
Find the minimum depth of the binary tree. The minimum depth is the number of nodes along the shortest path from root node to the nearest leaf node.

Min Depth: 2                                Min Depth: 3
        12                                              12
    7       1                                       7             1
        10      5                                      9      10      5     
                                                           11          
'''

from collections import deque

class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

# TC: O(n) SC: O(n) - BFS
def findMinDepthBFS(root):
    queue = deque()
    queue.append(root)

    curr_level = 1 # 1 because we already know root is there on level 1 and we already pushed it to the queue
    while len(queue):
        for i in range(0, len(queue)): # Pop all nodes for current level
            node = queue.popleft()

            if node.left is None and node.right is None:
                return curr_level
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        curr_level += 1

    return curr_level

# TC: O(n) SC: O(n) - DFS
def findMinDepthDFS(root):
    # If tree is empty return the minimum depth as 0
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1
    
    left = findMinDepthDFS(root.left) if root.left else float('inf')
    right = findMinDepthDFS(root.right) if root.right else float('inf')

    return 1 + min(left, right) # 1 + because root is always going to be there and then we add left and right's depth to it

root = Node(12)
root.left = Node(7)
root.left.left = Node(9)

root.right = Node(1)
root.right.left = Node(10)
root.right.right = Node(5)
root.right.left.left = Node(11)

print(findMinDepthDFS(root))

print(findMinDepthBFS(root))