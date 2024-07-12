'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''

'''
Approach for finding middle node:
Even: Return second middle node

Take 2 pointers slow and fast
Move slow by 1 step and fast by 2 steps only if:
    - fast is not the last node - We know that fast is at the last if fast's next is Null and
    - fast is not null i.e. fast didn't reach the null i.e. traversed the entire LL.
slow pointer would always point to the middle node of the linked list.


Approach for reversing the linked list:

We need to reverse the links.

Initial prev to none and current to head

loop till current is not None i.e. until we reach the end of the linked list

    point current's next to prev
    move current to current.next but for this we must save current.next to temp since we are altering the current.next to point to prev so if do directly curr = curr.next it will
    point to previous which is incorrect so that's why before modifying current.next save to temp else value would change and we can't move current ahead to work on other nodes.

    so, temp = current.next
    current.next = prev
    
    Now move prev to curr but this must be done before we move curr to curr.next i.e. before we do curr = temp else we loose curr node where we need to keep prev.
    so, prev = current

    now, current = temp (i.e. current = current.next(temp))

At the end the node where prev points is the newHead.
'''

# Reverse: TC: O(n) SC: O(1)
# Finding the middle node: TC: O(n) SC: O(1)

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def printLL(head):
   curr = head
   
   while curr is not None:
      print(curr.data, end = ' ')
      curr = curr.next

def reverseLL(head):
    prev = None
    curr = head

    while curr is not None:
       temp = curr.next
       curr.next = prev
       prev = curr
       curr = temp

    return prev

def findMiddleNode(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
       slow = slow.next
       fast = fast.next.next

    return slow

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
printLL(head)

mid = findMiddleNode(head)
print('\nMid Node:', mid.data)

head.next.next.next = Node(4)
printLL(head)

mid = findMiddleNode(head)
print('\nMid Node:', mid.data)

newHead = reverseLL(head)
printLL(newHead)