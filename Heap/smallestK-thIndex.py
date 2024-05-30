import heapq

'''
Given an array, find kth-smallest number from it.

arr = [3, 1, 5, 12, 2, 11]

Example find 3rd smallest number.
result = 3

since smallest consider building a max-heap
'''

arr = [3, 1, 5, 12, 2, 11]
k = 3

max_heap = []
for i in range(0, k):
    heapq.heappush(max_heap, -(arr[i]))

for i in range(k, len(arr)):
    if arr[i] < -(max_heap[0]):
        heapq.heappop(max_heap)
        heapq.heappush(max_heap, -(arr[i]))

for i in range(0, len(max_heap)):
    max_heap[i] = -(max_heap[i])

print('kth-index element =>', max_heap[0])