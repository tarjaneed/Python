'''
34. Find First and Last Position of Element in Sorted Array.

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
'''

# TC: O(log n) - since reducing the search by halves everytime.
# SC: O(1)

'''
Approach:

Sorted array and O(log n) -- so Binary Search.

left_most = -1
right_most = -1
we continue checking below till left is less than or equal to right; if left crosses right we break and return left_most and right_most indexes.
        left_most = findLeftMost()
        right_most = findRightMost()

        return [left_most, right_most]

    - Find the left most index for a given target

        The mid that matches target we consider it to be a possible answer and we check on left side further to find the 1st most possible index

        findLeftMost():
            l = 0
            r = n - 1
            
            while l < r:
                # Find mid

                mid = l + (r - l) / 2

                if nums[mid] == target:
                    left_most = mid
                    right = mid - 1
                else if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return left_most

    - Find the right most index for a given target:
            The mid that matches target we consider it to be a possible answer and we check on right side further to find the last possible index

            findRightMost():
                l = 0
                r = n - 1
                
                while l < r:
                    # Find mid

                    mid = l + (r - l) / 2

                    if nums[mid] == target:
                        right_most = mid
                        left = mid + 1
                    else if nums[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1

            return right_most

'''

def findLeftMost(n, nums, target):
    left_most = -1

    l = 0
    r = n - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            left_most = mid
            r = mid - 1 # To check left most
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return left_most


def findRightMost(n, nums, target):
    right_most = -1

    l = 0
    r = n - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            right_most = mid
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1 # To check right most

    return right_most

nums = [5, 7, 7, 8, 8, 10]
target = 8

n = len(nums)
left_most = findLeftMost(n, nums, target)
right_most = findRightMost(n, nums, target)

print(left_most, right_most)

nums = [5, 7, 7, 8, 8, 10]
target = 6

n = len(nums)

left_most = findLeftMost(n, nums, target)
right_most = findRightMost(n, nums, target)

print(left_most, right_most)