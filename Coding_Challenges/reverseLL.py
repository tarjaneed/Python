''' Problem 2: Reverse a Linked List
TC: O(n)

Question: How to change head and tail pointers after reversing the linked list '''

class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert(self, element):
    new_node = Node(element)

    if self.head == None:
      self.head = new_node
      self.tail = self.head
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = self.tail.next

  def printLinkedList(self):
    print('Linked List:')
    current = self.head
    while current:
      print(current.data)
      current = current.next

  def reverseLL(self):
    print('Reversed Linked List:')
    curr = self.tail
    while curr:
      print(curr.data)
      curr = curr.prev

linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)

linked_list.printLinkedList()
linked_list.reverseLL()