'''
Time Complexity & Space Complexity
    No of nodes * work done at each node (printing, deleteing, appendding) = O(n) * c = O(n) we are visting every node
    BFS Simple - O(n)
    Level Wise - O(n)
    Reversed using List / Queue - O(n)
'''

from collections import deque

class Node:

  def __init__(self, data):
    self.key = data
    self.left = None
    self.right = None

def insert(root, newKey):
  # Check if tree is empty; create root node if empty and return
  if root is None:
    root = Node(newKey)
    return root

  if newKey > root.key:
    root.right = insert(root.right, newKey)
  else:
    root.left = insert(root.left, newKey)

  return root

# Level Order Traversal
def BFSTraversal(root):
    queue = deque()
    result = []

    # Add root in the queue
    queue.append(root)

    while len(queue):
        node = queue.popleft() # Pop element on the first position in the queue
        result.append(node.key) # Append it to the result since it is traversed
        # Check for its left and right child and add them to the queue, so that they can be traversed in the next iteration(s)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def BFSLevelByLevel(root):
    queue = deque()
    result = []
    queue.append(root) # Add root to the queue

    while len(queue):
        curr_level = []
        for i in range(len(queue)):
            node = queue.popleft()
            curr_level.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(curr_level)
    return result

def reverseLevelTraversalByList(root):
    queue = deque()
    result = [] # result as a list
    queue.append(root) # Add root to the queue

    while len(queue):
        curr_level = []
        for i in range(len(queue)):
            node = queue.popleft()
            curr_level.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(curr_level)

    result = result[::-1]
    return result

def reverseLevelTraversalByQueue(root):
    queue = deque()
    result = deque() # result as a queue
    queue.append(root) # Add root to the queue

    while len(queue):
        curr_level = []
        for i in range(len(queue)):
            node = queue.popleft()
            curr_level.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.appendLeft(curr_level)

    return result

root = Node(10)
insert(root, 15)
insert(root, 5)
insert(root, 20)
insert(root, 2)
insert(root, 1)
insert(root, 13)
insert(root, 8)

bst_simple = BFSTraversal(root)
print(bst_simple)

bst_level_wise = BFSLevelByLevel(root)
print(bst_level_wise)

reverse_BFS = reverseLevelTraversalByList(root)
print('List', reverse_BFS)

reverse_BFS = reverseLevelTraversalByList(root)
print('Queue', reverse_BFS)