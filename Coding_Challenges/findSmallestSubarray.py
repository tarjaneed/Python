'''
Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray whose 
sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Example 1:
Input: [2, 1, 5, 2, 3, 2], S = 7
Output: 2

Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].
'''

# TC: O(n) SC: O(1)

def findSmallestSubarray(nums, targetSum):
    L = 0 # L and R are initialized to 0
    total = 0
    result = float('inf') # Stores the length of the minimum subarray

    for R in range(0, len(nums)):
        total += nums[R] # Keep suming the number we see

        # Check the condition if total >= sum/target; if it is move the Left pointer ahead
        # While is used because we want to keep checking if there is any more subarray we get with shorter length
        while total >= targetSum:
            result = min((R - L) + 1, result) # Update the result if current window is of min Length than the previous one
            total -= nums[L]
            L += 1

    return 0 if result == float('inf') else result

nums = [2, 1, 5, 2, 3, 2]
targetSum = 7
print(findSmallestSubarray(nums, targetSum))

nums = [1, 4, 4]
targetSum = 4
print(findSmallestSubarray(nums, targetSum))