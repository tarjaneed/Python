'''
Given an array of positive numbers and a positive number k, find the maximum sum of any contiguous subarray of size k.

Input = [2, 1, 5, 1, 3, 2] k = 3
Output = 9

Explanation: Subarray [5, 1, 3] has the maximum sum of 9
'''

# TC: O(n)

def findMaxSubArray(nums, k):
    w_s = 0
    w_e = 0

    sum = 0
    max_sum = 0

    for w_e in range(0, len(nums)):
        sum += nums[w_e]

        if w_e - w_s == k - 1:
            max_sum = max(max_sum, sum) # update the max_sum if the current calculated sum is greater than the previous max_sum value
            sum -= nums[w_s]
            w_s += 1

    return max_sum

nums = [2, 1, 5, 1, 3, 2]
k = 3
    
print(findMaxSubArray(nums, k))

nums = [1, 5, 4, 2, 9, 2, 1]
k = 3
    
print(findMaxSubArray(nums, k))

nums = []
k = 3
    
print(findMaxSubArray(nums, k))