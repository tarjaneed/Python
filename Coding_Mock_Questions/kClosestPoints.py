'''
Given an array of points in a 2D plane, find ‘K’ closest points to the origin.
Example 1:
Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5). The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
'''

'''
Since closest i.e. smallest we use maxheap 
We loop till we check all the points i.e. till len(points)
    for each point we calculate the euclidian distance and push it to the max heap

    since we need only k-closest points if the length of max_heap becomes > k that is given we pop from the heap i.e. it would remove the point that has larger distance

At the end we loop the heapq and return the points nearest since we pop everytime len(max_heap) becomes > k by the end we already have the k-closest points
'''

import math
import heapq

# TC: O(n * logk) SC: O(k) - at most k elements will be there in the heap

def kClosestPoints(points, k):

    max_heap = []

    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]

        distance = math.hypot(x, y)
        heapq.heappush(max_heap, (-distance, x, y))

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [[x, y] for d, x, y in max_heap]

points = [[1, 2], [1, 3]]
k = 1
print(kClosestPoints(points, k))

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosestPoints(points, k))