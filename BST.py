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
    if root.left is None:
      return root.right

    # Case 3 - If root has both left and right child
  return root

def search(root, key):
  if root is None:  # Ask why this is needed
    return None

  if root.key == key:
    return root

  if key > root.key:
    return search(root.right, key)
  else:
    return search(root.left, key)


def printBST(root):
  if root:
    printBST(root.left)
    print(root.key)
    printBST(root.right)


root = Node(10)
insert(root, 15)
insert(root, 5)
insert(root, 20)
insert(root, 2)
insert(root, 1)

printBST(root)  # 1 2 5 10 15 20

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

print('After Delete')
printBST(root)