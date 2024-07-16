'''
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.
The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. 
Formally, a building has an ocean view if all the buildings to its right have a smaller height.
Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

Example 1:
Input: heights = [4, 2, 3, 1]
Output: [0, 2, 3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
'''

'''
Approach:

Ocean is to the right so we start from last index and initialize the maxHeight as 0.

We loop from end to 0th index in reverse:
    we check height at the current index > maxHeight:
        if it is > we update maxHeight with this newHeight and add this index in the result meaning this buidling will have an ocean view

        if current_height < max_heigth: we do nothing it simply means that current building or index since it has less height than maxheight it would not have an ocean view
'''

# TC: O(n) SC: O(1) or O(n) if we consider queue as an additional space if all the buildings have a view

from collections import deque

def sortedIndices(heights):
    result = deque()
    n = len(heights)
    max_height = 0

    for i in range(n - 1, -1, -1):
        if heights[i] > max_height:
            result.appendleft(i)
            max_height = heights[i]

    return list(result)

heights = [4, 2, 3, 1]
print(sortedIndices(heights))

heights = [4, 3, 2, 1]
print(sortedIndices(heights))

heights = [1, 2, 3, 4]
print(sortedIndices(heights))