''''
153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
'''

'''
Approach:

Sorted array and to be done in O(logn) so Binary Search can be applied.

For any sorted array we know all the elements to the left are smaller than the element we consider (mid) and all the elements to the right are greater than mid.

- Initialize left = 0 and right = n - 1

Continue till left is less than right:
    - We find the mid
    - Compare it to the right;
        if mid > right (there is an issue); means our min element must be towards the right i.e the first rotation point.
            in this case we will check on the right; also the since the mid is greater than the right element we checked it can never the mininum element so we discard it
            l = mid + 1
        else:
            if arr[mid] < arr[right] it means current mid could be the answer and our mininum element is to the left.
            r = mid

return nums[r] or nums[l] # Since loop breaks when l becomes equal to r. 
            
Note: here we do left < right and not left <= right since we are considering mid as the possible answer so if we use = then we would be trapped in the loop; i.e. we keep calculating same mid and 
go in else condition so to avoid this we do left < right
'''

def findMinElement(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = (l + r) // 2

        if nums[mid] > nums[r]: # Problem
            l = mid + 1 # Move to check on right side
        else:
            r = mid # Mid could be the answer too and check on the left side

    return nums[r]

nums = [3, 4, 5, 1, 2]
print(findMinElement(nums))

nums = [4,5,6,7,0,1,2]
print(findMinElement(nums))

nums = [11,13,15,17]
print(findMinElement(nums))