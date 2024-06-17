'''
Write a function to sort the objects in-place on their creation sequence number.
Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
'''

# TC: O(n) SC: O(1)

# Here we keep swapping the numbers with its correct index and we only move ahead when we find the right spot for the first index; then we do the same thing for the subsequent indexes
def cyclic_sort(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1 # This retrives the correct index for the number we are checking

        if nums[i] != nums[j]:
            [nums[i], nums[j]] = [nums[j], nums[i]]
        # This executes when we get same numbers which indicates that we have that number at the correct position
        # for eg. we have nums[i] as 1 and so the j would become nums[i] - 1 which is 0 in this case nums[i] i.e. nums[0] and nums[j] i.e. nums[0] would result in the same number 
        # indicating the correct position
        else:
            i +=1 

    return nums

nums = [3, 1, 5, 4, 2]
print(cyclic_sort(nums))

nums = [2, 6, 4, 3, 1, 5]
print(cyclic_sort(nums))