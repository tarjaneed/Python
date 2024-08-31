'''
Subset Sum Count: Print the count of Sq which sums to K

Given a set of positive integers and an integer k, count non-empty subsets that sums to k.

Example:
Input: nums = [7, 3, 2, 5, 8], k = 14 
Output: 1 => Subset with the given sum exists Subset [7, 2, 5] sums to 14

Input: nums = [1, 2, 1]
Output: 2 => [1, 1], [2]
'''

# TC: At every index we have 2 choices - Either take or not take, so for n indexes - O(2 power n)
# SC: O(n) - Size of the input - at any given time max recursive calls waiting can be equal to that of the length of the input

'''
Approach:

Recursively:
    check for a subset in 2 cases:
        - when you pick an element
        - when you don't pick an element

at the end return summation of this both cases.
'''

def count_subsets(index, nums, sum, targetSum):
    if index == len(nums):
        if sum == targetSum:
            return 1

        # else
        return 0

    sum += nums[index]
    pick = count_subsets(index + 1, nums, sum, targetSum)
    
    sum -= nums[index]
    not_pick = count_subsets(index + 1, nums, sum, targetSum)

    return pick + not_pick

nums = [7, 3, 2, 5, 8]
targetSum = 14 
print(count_subsets(0, nums, 0, targetSum))

nums = [1, 2, 1]
targetSum = 2 
print(count_subsets(0, nums, 0, targetSum))