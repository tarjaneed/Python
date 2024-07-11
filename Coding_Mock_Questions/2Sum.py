'''
Two Sum: Here input array can be sorted or unsorted

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

'''
Approach:

Start i from 0 and go till length of nums list/array
Create a hash map to store the already seen element and its index and to also find the remanining number we calculate.
{element: index}

Find the remaining number i.e. subtract the current element number i.e. 2 from the target 9 = target - element = 9 - 2 = 7
Now, find the remaining number in the hashmap:
    if not found:
        we save the current element we have seen in it (save 2 and its index 0 in hashmap)
        move and check for the next i
    if found:
        we got our answer = index of remaining_number from hashmap, current ith index i.e {hashmap[remaining_number], current_i_index}
'''

# TC: O(n) since there is only 1 loop and we go through the array only once
# SC: O(n) - HashMap worst case all elements are stored and answer is not found

def twoSum(nums, target):
    seenHashMap = {}

    for i in range(len(nums)):
        remaining_number = target - nums[i]

        if remaining_number in seenHashMap:
            return [seenHashMap[remaining_number], i]
        else:
            seenHashMap[nums[i]] = i

    return []

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))