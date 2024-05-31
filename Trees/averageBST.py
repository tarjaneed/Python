'''
Given a binary tree, populate an array to represent the averages of all of its levels.

      1
   2    3
  4  5 6  7 
Level Averages: [1, 2.5, 5.5]

TC: O(n) SC: O(n)
'''

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

# Always returns a sorted order
def inOrderTraversal(root):
  if root is None:
    return
  
  inOrderTraversal(root.left)
  print(root.key, end=" ")
  inOrderTraversal(root.right)

def averageOfLevels(root):
    queue = []
    result = []

    queue.append(root) # Append root to the queue i.e. add first element to the queue

    # O(n) + O(n) = O(n)
    while len(queue):
        curr_level = []

        for _ in range(0, len(queue)): # O(n)
            node = queue.pop()
            curr_level.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(sum(curr_level) / len(curr_level)) # Instead of current levels we store average of that level - O(n)

    return result

root = Node(10)
insert(root, 15)
insert(root, 5)
insert(root, 20)
insert(root, 2)
insert(root, 1)
insert(root, 13)
insert(root, 8)

print('Average of Levels:')
print(averageOfLevels(root)) # 1 2 3 4 5 6 7

