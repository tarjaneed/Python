'''
Connect N Ropes With Minimum Cost
Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. The cost of connecting two ropes is equal to the sum of their lengths.

Example 1:
Input: [1, 3, 11, 5]
Output: 33
Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)
'''

'''
Approach:

1. We start by pushing all the elements into the min-heap.
2. Then we iterate till we have elements in the heap
    - We take first and 2nd element; sum them and add the sum to the min-heap
    - We also keep saving this sum in the result to add up cost from each step

Start by connecting 2 ropes and then combine all the 2 ropes sum each to the resultant sum for calculating for one big rope
            1
        3       5
    11


        4 (1 + 3)
    5       11

    9 (5 + 4)
11

    20 (9 + 11)

= 4 + 9 + 20 = 33

'''

import heapq

# TC: O(nlogn) (push - logn and we do it n times) + O(nlogn) + O(nlogn) - pop = O(nlogn)
# SC: O(n) - at any point there would be n ropes even if we add sum of 2 ropes

def findMinCost(ropes):

    if len(ropes) == 0:
        return 0
    
    if len(ropes) == 1:
        return ropes[0]
    
    minCost = 0
    min_heap = []

    for i in range(len(ropes)):
        heapq.heappush(min_heap, ropes[i])
    
    # Till we have 2 ropes to sum else it would continue infintely
    while len(min_heap) > 1:
        first_element = heapq.heappop(min_heap)
        second_element = heapq.heappop(min_heap)

        currCost =  first_element + second_element
        minCost += currCost

        heapq.heappush(min_heap, currCost)

    return minCost

ropes = [1, 3, 11, 5]
print(findMinCost(ropes))