'''
2 Sum - II - Input Array is sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
'''

'''
Approach:
2 Pointers Increment and Decrement Technique

Given: Array is sorted and no extra space to be used so cannot use hashmap

Take 2 pointers: i = 0 and j = len(array) - 1

Continue till i doesn't cross j why because if they cross they would again keep checking same numbers i.e. i would check the ones after checked by j and vice-versa.
Also when i crosses j we know we didn't find the answer so return [] and if i > j i.e. if i crosses j it means we have already seen all the elements.
Also i <= j would be issue since it would check same element at one point which might lead to incorrect result lets both point to 2 and target is 4 then this would be wrong. 

While i < j:
    take sum of ith and jth element and compare it with the target given
    if sum < target:
        we need bigger values moving forward to reach our target
        so we do increment i since array is sorted incrementing i would give us bigger values
    else if sum > target:
        we need smaller number moving forward to reach our target
        so we decrement j and array is sorted so decrementing j would give us smaller values
    else if sum == target:
        we got our answer and we return index i and index j with + 1 to them since 1-indexed is mentioned
'''

# TC: O(n)
# SC: O(1)

def twoSumSorted(nums, target):
    n = len(nums)

    i = 0
    j = n - 1

    while i < j:
        sum = nums[i] + nums[j]

        if sum > target:
            j -= 1
        elif sum < target:
            i += 1
        else:
            return [i + 1, j + 1]

    return []


numbers = [2, 7, 11, 15]
target = 9
print(twoSumSorted(numbers, target))

numbers = [2, 3, 4]
target = 6
print(twoSumSorted(numbers, target))

numbers = [-1, 0]
target = -1
print(twoSumSorted(numbers, target))