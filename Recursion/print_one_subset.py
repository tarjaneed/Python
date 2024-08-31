'''
Print only 1st Sq which sums to K

Subset Sum: Print any 1 Subset or Subsequence which sums to K
Given a set of positive integers and an integer k, check if there is any non-empty subset that sums to k and return any one of it.

Example:
Input: nums = [7, 3, 2, 5, 8], k = 14 
Output: [7, 2, 5] => Subset with the given sum exists Subset [7, 2, 5] sums to 14

Input: nums = [1, 2, 1]
Output: [1, 1] or [2]
'''

# TC: O(2 power n) in worst case it is possible that we find the subset after checking all the combinations and not at the start itself; if found early it might not have to do 2 power n checks.
# SC: O(n) - Size of the input - worst can be to check all the elements in the input to be included in the subset and then we find the answer.

def print_subset(index, subseq, nums, sum, targetSum):
    global output
    if index == len(nums):
        if sum == targetSum:
            output.append(subseq.copy())
            return True
        return False
    
    subseq.append(nums[index])
    sum += nums[index]
    if (print_subset(index + 1, subseq, nums, sum, targetSum) == True):
        return True

    subseq.pop()
    sum -= nums[index]
    if (print_subset(index + 1, subseq, nums, sum, targetSum) == True):
        return True

    return False

global output

output = []
nums = [7, 3, 2, 5, 8]
targetSum = 14 
print_subset(0, [], nums, 0, targetSum)
print(output)

output = []
nums = [1, 2, 1]
targetSum = 2 
print_subset(0, [], nums, 0, targetSum)
print(output)