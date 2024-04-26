'''
Bisect: Built-in Binary Search Method. Used to search for an element in the list but the list must be sorted
'''

import bisect

list1 = [1, 2, 3, 3, 5, 6, 6, 6, 7]

print(bisect.bisect_left(list1, 3)) # Returns 2 i.e. first index occurence of element 3

index = bisect.bisect_right(list1, 3) # Returns 4 i.e. last index occurence of element 3 + 1 => to insert the element in the sorted order

list1.insert(index, 4)

print(list1)

bisect.insort_left(list1, 3) # Inserts 3 at the leftmost index before exisitng 3

print(list1)

bisect.insort_right(list1, 6) # Inserts 3 at the rightmost index after exisitng 6

print(list1)
