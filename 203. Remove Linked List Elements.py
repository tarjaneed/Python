'''
203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
'''

'''
Approach:

- If we find the matching val with the node at the starting of the linked list, we keep shifting and updating the head till we find a non-matching value.
- After that we are sure that head is at its correct place, so now we check in the rest of the linked list to remove the matching val:
    Keep prev = None and current = head
    We continue till current is not None:
        if current.val == val: We move current to the next node and we also update prev's next to this new current this way we break link between matching val.
            current = current.next
            prev.next = current
        else: # Keep moving prev to current and current to current.next
            prev = current
            current = current.next

    return head # At the end return head
'''

# TC: O(n) SC: O(1)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def printLL(head):
    current = head

    if current is None:
        print([])

    while current:
        print(current.val, end=" ")
        current = current.next

def removeElements(head, val):
    while head and head.val == val:
        head = head.next

    current = head
    prev = None

    while current:
        if current.val == val:
            current = current.next
            prev.next = current
        else:
            prev = current
            current = current.next

    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(6)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(6)
newHead = removeElements(head, 6)
printLL(newHead)

print('\n')

head = None
newHead = removeElements(head, 1)
printLL(newHead)

print('\n')

head = Node(7)
head.next = Node(7)
head.next.next = Node(7)
head.next.next.next = Node(7)
newHead = removeElements(head, 7)
printLL(newHead)