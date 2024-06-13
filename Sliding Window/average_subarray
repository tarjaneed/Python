'''
Given an array, find the average of each subarray of K contiguous elements in it.

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K = 5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
'''

# TC: O(n)

def findAverage(nums, k):
    w_s = 0 # Window Start
    w_e = 0 # Window End

    sum = 0 # Holds the sum as we traverse
    result = []

    # Loop till window end reaches end of the list
    for w_e in range(0, len(nums)):
        sum += nums[w_e] # Keeps the sum stored avoids re-calculation - sums or add the element to the sum that we current traverse

        # if the current window hits the given k window size then perform the given action i.e. average k - 1 because index starts from 0 so it k = 5 then we go till 4 and not 5.
        # Then remove the nums[w_s] from sum since we would be moving the start pointer ahead and we do not want to re-calculate sum so we just remove it and then add for w_e to sum 
        # in next iteration. We remove from sum first because if we increase w_s and then do it we would remove the wrong element i.e. we would loose the index.
        if w_e - w_s == k - 1:
            result.append(sum / k)
            sum -= nums[w_s]
            w_s += 1
    
    return result

nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

print(findAverage(nums, k))

nums = [1, 3, 2]
k = 3

print(findAverage(nums, k))