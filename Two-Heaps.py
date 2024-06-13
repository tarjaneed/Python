'''
The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

For example:

For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5

Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.
'''

# TC: O(1) to find the meadian

import heapq

small = [] # Max Heap - holds smaller values and we need max from those smaller values at the top
large = [] # Min Heap - holds the larger values and we need min value from those larger values at the top

# O(logn)
def add(num):
    # By default we add to the small heap
    heapq.heappush(small, -1 * num) # Since max heap needs to be build so store negative values

    # We need to check first if small has values less than large to move elements; then check uneven length or size to move elements; Order of checking is important to avoid imbalance
    # Check if values in the small heap is lesser than the values in the large heap or not; if not we move the elements
    if small and large and (-1 * small[0]) > large[0]:
        val = - 1 * heapq.heappop(small)
        heapq.heappush(large, val)

    # Uneven size: Now check if difference between small and large heap exceeded 1 or not; if it did we need to re-balance and move to the root element to the large heap
    if len(small) - len(large) > 1: # Difference is 2 or more
        # Remove the root element from the small heap and add to large heap to re-balance
        val = - 1 * heapq.heappop(small)
        heapq.heappush(large, val)

    if len(large) - len(small) > 1:
        val = heapq.heappop(large)
        heapq.heappush(small, -1 * val)

# O(1)
def findMedian():
    # Odd who ever has larger length top of that is the median
    # If small heap has larger length then it's root is the median
    if len(small) > len(large):
        return -1 * small[0] # Return max value from min numbers
    elif len(large) > len(small):
        return large[0] # Return min value from max numbers
    else:
        # Even - both small and large have same length i.e. same number of elements
        # Take max from small and min from large i.e. take top elements from both and divide it by 2 to get the median
        return ((-1 * small[0]) + large[0]) / 2

add(1)
add(2)
add(3)
print(findMedian())
add(7)
print(findMedian())