'''
Subset Sum: Print all Sq which sums to K
Given a set of positive integers and an integer k, check if there is any non-empty subset that sums to k.

Example:
Input: nums = [7, 3, 2, 5, 8], k = 14 
Output: Subset with the given sum exists Subset [7, 2, 5] sums to 14

Input: nums = [1, 2, 1]
Output: [1, 1], [2]
'''

# TC: At every index we have 2 choices - Either take or not take, so for n indexes - O(2 power n)
# SC: O(n) - Size of the input - at any given time max recursive calls waiting can be equal to that of the length of the input

def subset_sum(index, subseq, nums, sum, targetSum):
    global output
    if index == len(nums):
        if sum == targetSum:
            output.append(subseq.copy())
        return

    # consider current index element
    subseq.append(nums[index])
    sum += nums[index]
    subset_sum(index + 1, subseq, nums, sum, targetSum)

    # do not consider current index element
    subseq.pop()
    sum -= nums[index]
    subset_sum(index + 1, subseq, nums, sum, targetSum)

global output
output = []
nums = [7, 3, 2, 5, 8]
targetSum = 14 

subset_sum(0, [], nums, 0, targetSum)
print(output)

output = []
nums = [1, 2, 1]
targetSum = 2 

subset_sum(0, [], nums, 0, targetSum)
print(output)