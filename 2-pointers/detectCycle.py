'''
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not. Return true if we find a cycle.

Straight list -> No Cycle
Last node's next pointer connected to some other node -> Cycle
'''

'''
TC: O(n) - Just traversing the linked list; moving the pointers and comparing them to check if they are equal
SC: O(1)
'''

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

    def detectCycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next: # Till fast is not none we keep moving pointers and comparing no need to check slow as it is always going to be behind fast or equal - fast.next not needed for even numbers but needed for odd
            slow = slow.next # Increments by 1 Step
            fast = fast.next.next # Increments by 2 Steps

            # Loop break condtion when both the pointers are at same index we know we found a cycle
            if slow == fast:
                return True

        return False # When fast is none it exists while and comes here so we know there is no cycle found and straight Linked List end with a None/Null

linked_list1 = LinkedList()

linked_list1.insertAtEnd(1)
linked_list1.insertAtEnd(2)
linked_list1.insertAtEnd(3)
linked_list1.insertAtEnd(4)
linked_list1.insertAtEnd(5)

linked_list1.printLinkedList()
print('\nStraight List Cycle Found:', linked_list1.detectCycle())

linked_list1.insertAtEnd(6)
linked_list1.printLinkedList()

linked_list1.head.next.next.next.next.next = linked_list1.head.next.next # 1 - 2 - 3 - 4 - 5 - 6 - 3  i.e. 6 is connected back to 3
print('\nLooped List Cycle Found:', linked_list1.detectCycle())

# Created a loop for testing
linked_list1.head.next.next.next = linked_list1.head # 1 - 2 - 3 - 4  - 1 i.e. 4 is connected back to 1
print('Looped List Cycle Found:', linked_list1.detectCycle())