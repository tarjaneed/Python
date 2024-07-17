'''
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
Example 1:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null Output: true
'''

'''
Approach:

Step - 1. Find the 2nd half of the linked list or middle of the linked list
    Use slow and fast pointers; move slow by 1 and fast by 2 steps
    Consider both odd and even and continue only if both conditions are true i.e. either fast is at last node (odd) or at 2nd last node (even)
        Even - Take M1 instead of M2 so the fast should go till 2nd last node i.e. fast.next.next = None
        Odd - Fast will go till the last node i.e. fast.next = None
    At the end the node to which slow points is the middle node. Return slow pointer.
Step - 2:
    Now reverse the 2nd half of the linked list pass head as slow.next
    Save the newHead the function returns
Step - 3:
    Compare the first half with second half till second half reaches null
    first = head and second = newHead

    if first.data != second.data
        return False # LL is not a palindrome
    otherwise if they match go ahead and check other nodes
        move first to next
        and second to next
If we come out of the loop we know all comparisons were valid i.e. LL is palindrome
'''

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def printLL(head):
   curr = head

   while curr is not None:
      print(curr.data, end = ' ')
      curr = curr.next

def reverseSecondHalf(head):
    current = head
    prev = None

    while current is not None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

# TC: O(n) SC: O(1)

def checkIsPalindrome(head):
    # Edge cases
    # If linked list is empty it's a palindrome
    if head is None:
       return True
    
    # If there is only one node
    if head.next is None:
       return True

    # Find Middle Node
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    newHead = reverseSecondHalf(slow.next)

    # Compare first half and second half
    first = head
    second = newHead

    while second is not None:
        if first.data != second.data:
            reverseSecondHalf(newHead) # If asked to maintain the input given and return it unchanged
            return False
        first = first.next
        second = second.next

    reverseSecondHalf(newHead) # If asked to maintain the input given and return it unchanged
    return True

head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)

printLL(head)
print(checkIsPalindrome(head))

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

printLL(head)
print(checkIsPalindrome(head))

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(3)

printLL(head)
print(checkIsPalindrome(head))

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(3)
head.next.next.next.next = Node(1)
head.next.next.next.next.next = Node(1)

printLL(head)
print(checkIsPalindrome(head))


head = None

printLL(head)
print(checkIsPalindrome(head))

head = Node(1)

printLL(head)
print(checkIsPalindrome(head))