import heapq

'''
Given an unsorted array of numbers, find k-smallest numbers from it.

arr = [3, 1, 5, 12, 2, 11] k = 3
result = [1, 2, 3] => Order can be any

since smallest consider max heap

TC: O(N) + O(Nlogk) = O(Nlogk)
'''

arr = [3, 1, 5, 12, 2, 11]
k = 3

# TC: O(N); Build max heap with first k elements i.e. of 3 elements in this case
# To build max heap using the heapq we need to negate the values first
max_heap = []
for i in range(0, k):
    heapq.heappush(max_heap, -(arr[i]))

# Check rest of the elements in arr with the root; if element < root, we pop root and push this new element; else we check next elements
# By the time we reach end of the list the heap will have 3 smallest elements

# TC: O(Nlogk)
for i in range(k, len(arr)): # O(N - k) = O(N)
    if arr[i] < -(max_heap[0]):
        heapq.heappop(max_heap) # Remove the root element of heap - max element; O(log n) i.e. O(log k) => because we consider k elements out of n instead of entire n
        heapq.heappush(max_heap, -(arr[i]))  # O(log n) i.e. O(log k) => because we consider k elements out of n instead of entire n

for i in range(0, len(max_heap)):
    max_heap[i] = -(max_heap[i])

print(max_heap)
