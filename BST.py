# Implement Binary Search Tree with Operations: Seärch, Insert, Delete

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

def findMinValueNode(root, key):
  min = root
  while min.left:
    min = root.left

  return min

def delete(root, key):
  if root is None:
    return root

  # Find the node
  if key < root.key:
    root.left = delete(root.left, key)
  elif key > root.key:
    root.right = delete(root.right, key)
  else:
    # Case 1 - if root has no child or no left or right child
    # if root has left child but no right child
    if root.right is None:
      return root.left
    # if root has right child but no left child
    elif root.left is None:
      return root.right
    # Case 3 - If root has both left and right child - Find min value node in the right side of the root node which is the left most node within the right side or right subtree
    else:
      minNode = findMinValueNode(root.right, key)
      root.value = minNode.val
      root.right = delete(root.right, minNode.val)
  return root

def search(root, key):
  if root is None:
    
    return None

  if root.key == key:
    return root

  if key > root.key:
    return search(root.right, key)
  else:
    return search(root.left, key)

# Always returns a sorted order
def inOrderTraversal(root):
  if root is None:
    return
  
  inOrderTraversal(root.left)
  print(root.key, end=" ")
  inOrderTraversal(root.right)

def preOrderTraversal(root):
  if root is None:
    return
  print(root.key, end=" ")
  preOrderTraversal(root.left)
  preOrderTraversal(root.right)

def postOrderTraversal(root):
  if root is None:
    return
  postOrderTraversal(root.left)
  postOrderTraversal(root.right)
  print(root.key, end=" ")

root = Node(10)
insert(root, 15)
insert(root, 5)
insert(root, 20)
insert(root, 2)
insert(root, 1)
insert(root, 13)
insert(root, 8)

print('InOrder Traversal:')
inOrderTraversal(root)  # 1 2 5 8 10 13 15 20

print('\nPreOrder Traversal:')
preOrderTraversal(root)  # 10 5 2 1 8 15 13 20

print('\nPostOrder Traversal:')
postOrderTraversal(root)  # 1 2 8 5 13 20 15 10

print('\n\nSearch Execution:')

key = 20
if search(root, key) is None:
  print(key, 'Not Found')
else:
  print(key, 'Found')

key = 25
if search(root, key) is None:
  print(key, 'Not Found')
else:
  print(key, 'Found')

key = 2
if search(root, key) is None:
  print(key, 'Not Found')
else:
  print(key, 'Found')

root = delete(root, 1)

print('\nAfter Delete')
inOrderTraversal(root)