'''
Top K Frequent Elements

Input: [1, 3, 5, 12, 11, 12, 11], k = 2
Output: [12, 11]

Input: [5, 12, 11, 3, 11], k = 2
Output: [11, 3] or [11, 5] or [11, 12]

Approach 2: Using min-heap because we need to find frequent elements which means ones with the highest count
since highest we go for min-heap

- Count frequency of each element and store in a hashmap O(n)
- Then iterate through the hasmap and keep on pushing the freq, item tuple into the min heap. Heappush will re-order the elements keeping the element
with the mininum frequency as the root
- Once the min heap length exceeds the k we delete the root since anyway it is the element with min freq and we want the ones with max frequency.
- By the time we reach the end the min heap will have k-most frequent elements. 
'''

# TC: O(n) + O(n logk + logK) = O(nlogk)

import heapq

def findFrequentElements(arr, k):
    freq_count = {}

    for i in range(0, len(arr)):
        if arr[i] not in freq_count.keys():
            freq_count[arr[i]] = 1
        else:
            freq_count[arr[i]] += 1

    # Build a min heap with first k-elements
    min_heap = []
    for element, frequency in freq_count.items(): # O(n)
        heapq.heappush(min_heap, (element, frequency)) # O(logk) at a time min-heap will have only k-elements to process

        if len(min_heap) > k:
            heapq.heappop(min_heap) # O(logk)
    
    return [num for (num, count) in min_heap] # Shorthand to convert iterate over list of tuples and return the element in the list or an array

nums = [1, 3, 5, 12, 11, 12, 11]
k = 2

print(findFrequentElements(nums, k))

nums = [5, 2, 11, 3, 11]
k = 2

print(findFrequentElements(nums, k))