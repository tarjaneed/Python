import heapq

'''
Given an unsorted array of numbers, find k-largest numbers from it.

arr = [3, 1, 5, 12, 2, 11] k = 3
result = [5, 11, 12] => Order can be any

since largest consider min heap

TC: O(N) + O(Nlogk) = O(Nlogk)
'''

arr = [3, 1, 5, 12, 2, 11]
k = 3

# TC: O(N); Build min heap with first k elements i.e. of 3 elements in this case
min_heap = []
for i in range(0, k):
    min_heap.append(arr[i])

heapq.heapify(min_heap) # Creates a min-heap with first k-elements

'''
for i in range(0, k):
    heapq.heappush(min_heap, arr[i])
'''

# min-heap root is always the minimum element
# Check rest of the elements in arr with the root; if element > root, we pop root and push this new element; else we check next elements
# By the time we reach end of the list the heap will have 3 largest elements

# TC: O(Nlogk)
for i in range(k, len(arr)): # O(N - k) = O(N)
    if arr[i] > min_heap[0]:
        heapq.heappop(min_heap) # Re-orders the heap; Remove the root element of heap - min element; O(log n) i.e. O(log k) => because we consider k elements out of n instead of entire n
        heapq.heappush(min_heap, arr[i])  # Re-orders the heap; O(log n) i.e. O(log k) => because we consider k elements out of n instead of entire n

print(min_heap)