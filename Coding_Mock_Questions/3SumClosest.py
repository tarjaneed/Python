'''
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.
Example 1:
Input: [-2, 0, 1, 2], target = 2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
'''

'''
Approach:

- Since the sum is asked and not the index we can sort the input array so we can apply the 2-pointers technique.
- we initialize closestSum = 100000 to some bigger value
- for k = 0 to len(arr) - 2 (preferred) or n since we need 3 numbers so moving k till end wouldn't make any difference
    - We can fix a number i.e. k = 0 iteration and apply two pointers on the rest of the array until i < j and try to find the closestSum; 
    then we fix other number for iteration k = 1 and apply 2 pointers on rest of array until i < j and try to find the closestSum.

    Update the closest sum if the difference betweeen target and current sum we check is < than the difference between target and the prev closestSum we have so far i.e. 
    We try to find the sum that is near to the target. We need to return sum and not the difference but in order to know the closest sum we need to do the difference and choose 
    the min difference once sum.

    - 2 Pointers:
        i = k + 1
        j = len(arr) - 1

        sum = nums[k] + nums[i] + nums[j]

        if sum > target:
            j--
        else:
            i++
        
        if abs(target - sum) < abs(target - closestSum):
            closestSum = sum

- return closestSum
'''

# TC: Sort - O(nlogn) + O(n ^ 2) = O(n^2) SC: O(1) - In place sort

def findClosestSum(nums, target):
    closestSum = float('inf') # Max Value

    n = len(nums)

    nums.sort()

    for k in range(0, n - 2): # range(0, n) works too; Fix a number nums[k] and apply 2 pointers on rest of array i.e. in each iteration different number of k = 0, 1, 2... gets fixed
        i = k + 1
        j = n - 1

        # For this inner loop for each iteration based on k nums[k] will be same - this is what fixing a number is.
        while i < j:
            sum = nums[k] + nums[i] + nums[j]

            if sum > target:
                j -= 1
            else:
                i += 1
            
            if abs(target - sum) < abs(target - closestSum):
                closestSum = sum
        
    return closestSum

nums = [-2, 0, 1, 2]
target = 2

print(findClosestSum(nums, target))

nums = [-1, 2, 1, -4]
target = 1
print(findClosestSum(nums, target))

nums = [0, 0, 0]
target = 1
print(findClosestSum(nums, target))