'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6] 

Explanation: The linked-lists are: [1->4->5, 1->3->4, 2->6]
merging them into one sorted list: 1->1->2->3->4->4->5->6

'''

'''
Approach:

Merge Sort - Divice and Conquer

- Break the list into 2 halves based on mid: mid = (end - start) // 2
    Base Case:
        if start == end: # Meaning we only have 1 list or 1 list element
            return lists[start] 
- Keep on partitioning the lists till we reach 1 list i.e. the base case and then apply merging of 2 lists:
    L1 = partitionAndMerge(start, mid, lists)
    L2 = partitionAndMerge(start, mid, lists)

    return merge2Lists(L1, L2)

- merge 2 lists:
    Base cases:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

    if l1 < l2 we know the result would start from l1 hence we return l1 else l2
        we again call merge2lists recursively till the base is hit.
        so in l1->next we assign whatever is returned from merge2lists(l1->next, l2)
        we basically call same funtion on l1->next and l2 to do sorting
    else:
        we again call merge2lists recursively till the base is hit.
        so in l2->next we assign whatever is returned from merge2lists(l1, l2->next)
        we basically call same funtion on l1->next and l2 to do sorting
'''

# TC: O(n * logK) = logk levels and n amount of work done on each level

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    current = head

    while current is not None:
        print(current.data, end = " ")
        current = current.next

def merge2Lists(list1, list2):

    if list1 is None:
        return list2
    
    if list2 is None:
        return list1

    if list1.data < list2.data:
        list1.next = merge2Lists(list1.next, list2)
        return list1
    else:
        list2.next = merge2Lists(list1, list2.next)
        return list2

def partitionAndMerge(start, end, lists):
    if start == end:
        return lists[start]
    
    if start > end:
        return None

    mid = (end - start) // 2

    L1 = partitionAndMerge(start, mid, lists)
    L2 = partitionAndMerge(mid + 1, end, lists)

    return merge2Lists(L1, L2)

def mergeKLists(lists):
    n = len(lists)

    if n == 0:
        return None

    return partitionAndMerge(0, n - 1, lists)

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

linked_list_1 = Node(1)
linked_list_1.next = Node(4)
linked_list_1.next.next = Node(5)

linked_list_2 = Node(1)
linked_list_2.next = Node(3)
linked_list_2.next.next = Node(4)

linked_list_3 = Node(2)
linked_list_3.next = Node(6)

linked_lists = [linked_list_1, linked_list_2, linked_list_3]

printLL(mergeKLists(linked_lists))