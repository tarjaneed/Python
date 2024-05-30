'''
Top K Frequent Elements

Input: [1, 3, 5, 12, 11, 12, 11], k = 2
Output: [12, 11]

Input: [5, 12, 11, 3, 11], k = 2
Output: [11, 3] or [11, 5] or [11, 12]

Approach 1: O(nlogn)

- Count frequency of each element and store in a hashmap O(n)
- Perform sorting on it in desc order which brings highest counts elements to the beginning. O(n logn)
- Then take first k elements from that list/result.
'''

def findFrequentElements(arr, k):
    freq_count = {}

    for i in range(0, len(arr)):
        if arr[i] not in freq_count.keys():
            freq_count[arr[i]] = 1
        else:
            freq_count[arr[i]] += 1

    sorted_freq_count = sorted(freq_count.items(), key = lambda item: item[1], reverse = True)

    print(sorted_freq_count)

    frequent_elements = []
    for element, freq in sorted_freq_count:
        frequent_elements.append(element)

    return frequent_elements[:k] # Split to get the first k elements

nums = [1, 3, 5, 12, 11, 12, 11]
k = 2

print(findFrequentElements(nums, k))

nums = [5, 12, 11, 3, 11]
k = 2

print(findFrequentElements(nums, k))