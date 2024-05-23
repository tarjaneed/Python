'''
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
Example 1:
* Input: [1, 2, 3, 4, 6], target=6
* Output: [1, 3]
* Explanation: The numbers at index 1 and 3 add up to 6: 2 + 4 = 6
'''

'''
Since it is sorted we can use 2 pointers.
If it is not sorted we need to make use of a hashMap
'''

'''
TC: O(n) we are just traversing the list; finding sum and comparing
SC: O(1)
1. Initialize left and right ptrs
2. Loop till left < right
    1. Find sum of left + right and compare it with the target
    2. If sum == target return the current indices of left and right
    3. Else check if sum is greater than target then decrement the right pointer
    4. Else check if sum is smaller than target then increment the left pointer
'''

def twoSum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            return [left, right]
        elif sum > target:
            right -= 1 # Because we need a smaller number
        else:
            left += 1 # Becase we need a larger number
    return [-1, -1] # When target is not found


nums = [1, 2, 3, 4, 6]

target = 6
print(twoSum(nums, target))

target = 19
print(twoSum(nums, target))

target = 9
print(twoSum(nums, target))