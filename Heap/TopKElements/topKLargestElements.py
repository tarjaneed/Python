import heapq

'''
Given an unsorted array of numbers, find k-largest numbers from it.

arr = [3, 1, 5, 12, 2, 11] k = 3
result = [5, 11, 12] => Order can be any

since largest consider min heap
'''

arr = [3, 1, 5, 12, 2, 11]
k = 3

# Build min heap with first k elements i.e. of 3 elements in this case
list1 = []
for i in range(0, k):
    list1.append(arr[i])

heapq.heapify(list1) # Creates a min-heap with first k-elements

# Check rest of the elements in arr with the root; if element > root, we pop root and push this new element; else we check next elements
# By the time we reach end of the list the heap will have 3 largest elements

# TC: O(Nlogk)
for i in range(k, len(arr)): # O(N - k) = O(N)
    if arr[i] > list1[0]:
        heapq.heappop(list1) # Remove the root element of heap - min element; O(log n) i.e. O(log k) => because we consider k elements out of n instead of entire n
        heapq.heappush(list1, arr[i])  # O(log n) i.e. O(log k) => because we consider k elements out of n instead of entire n

print(list1)