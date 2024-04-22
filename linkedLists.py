# Create a Node Class

class Node:
  # Initializations
  def __init__(self, data):
    self.data = data
    self.next = None  # Pointer holding address to the next node


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = self.head

  def insertAtEnd(self, element):
    new_node = Node(element)  # Create a new node

    # Check if linked list is empty
    if self.head is None:
      self.head = new_node
      self.tail = self.head
    else:
      self.tail.next = new_node
      self.tail = self.tail.next

  def insertInBeginning(self, element):
    new_node = Node(element)
    new_node.next = self.head
    self.head = new_node

  def insertAtIndex(self, index, element):
    new_node = Node(element)

    i = 0
    current = self.head

    # If Index given is 0
    if index == 0:
      self.insertInBeginning(element)
      return

    while i != index:
      current = current.next
      i += 1

    temp = current.next
    current.next = new_node
    new_node.next = temp

    # If Index given is last one
    if current == self.tail:
      self.tail = current.next

  def updateELement(self, index, value):
    i = 0
    current = self.head

    while i != index:
      i += 1
      current = current.next

    current.data = value

  def removeFromEnd(self):
    current = self.head

    while (current.next.next):
      current = current.next

    self.tail = current
    self.tail.next = None

  def removeFromStart(self):
    self.head = self.head.next

  def removeFromMiddle(self, index):
    i = 0
    current = self.head

    # If Index given is 0
    if index == 0:
      self.removeFromStart()
      return

    while i != index - 1:
      current = current.next
      i += 1

    current.next = current.next.next

    # If Index given is last one
    if current.next == None:
      self.tail = current

  def printLinkedList(self):
    print('Linked List:')
    current = self.head
    while current:
      print(current.data)
      current = current.next


linked_list1 = LinkedList()

linked_list1.insertAtEnd(1)
linked_list1.insertAtEnd(2)
linked_list1.insertAtEnd(3)

linked_list1.printLinkedList()  # 1 2 3

linked_list1.insertInBeginning(5)

linked_list1.printLinkedList()  # 5 1 2 3

linked_list1.insertAtIndex(2, 20)

linked_list1.printLinkedList()  # 5 1 2 20 3

linked_list1.insertAtIndex(0, 10)

linked_list1.printLinkedList()  # 10 5 1 2 20 3

linked_list1.removeFromEnd()

linked_list1.printLinkedList()  # 10 5 1 2 20

linked_list1.removeFromStart()

linked_list1.printLinkedList()  # 5 1 2 20

linked_list1.removeFromMiddle(2)

linked_list1.printLinkedList()  # 5 1 20

linked_list1.removeFromMiddle(2)

linked_list1.printLinkedList()  # 5 1

linked_list1.updateELement(1, 200)
linked_list1.printLinkedList()  # 5 200