'''
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList. If the total number of nodes in the LinkedList is even, 
return the second middle node.
Example 1:
	Input: 1-> 2-> 3-> 4-> 5 -> null
	Output: 3
Example 2:
	Input: 1-> 2-> 3-> 4-> 5-> 6-> null
	Output: 4

Approach: Slow and Fast Pointer

- Point slow and fast pointer to the head
- Continue till fast has value and fast.next is not null meaning we need to stop at the last node and not go out of bounds for fast pointer
    - Move slow by one step and fast by 2 steps
'''

# TC: O(n) SC: O(1)

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

    def printLinkedList(self):
        print('Linked List:')
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

    def findMiddleNode(self):
        s = self.head
        f = self.head

        while f is not None and f.next is not None: # Stops at the last node we do not need to go out of bounds
            s = s.next
            f = f.next.next
        
        return s.data

linked_list1 = LinkedList()

linked_list1.insertAtEnd(1)
linked_list1.insertAtEnd(2)
linked_list1.insertAtEnd(3)
linked_list1.insertAtEnd(4)
linked_list1.insertAtEnd(5)

linked_list1.printLinkedList()

midNode = linked_list1.findMiddleNode()
print('\nMid of the linked list =>', midNode)

linked_list1.insertAtEnd(6)
linked_list1.printLinkedList()

midNode = linked_list1.findMiddleNode()
print('\nMid of the linked list =>', midNode)