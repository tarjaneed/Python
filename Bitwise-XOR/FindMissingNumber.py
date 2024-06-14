'''
Given an array of n-1 integers in the range from 1 to n, find the one number that is missing from the array

Input: [1, 5, 2, 6, 4]
Output: 3
'''

'''
Approach:
[1, 2, 3, 4, 5, 6] XOR [1, 5, 2, 6, 4]
= 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 1 ^ 5 ^ 2 ^ 6 ^ 4
= 0 ^ 3
= 3
'''

# TC: O(n)

nums = [1, 5, 2, 6, 4]
n = len(nums) + 1 # 6

# XOR 1 to n integers
x1 = 1
for i in range(2, n + 1): # n + 1 since stop is not included so if keep n it will go till 5 only and we need 6
    x1 = x1 ^ i

# XOR integers in input array
x2 = nums[0]
for i in range(1, n - 1):
    x2 = x2 ^ nums[i]

print(x1 ^ x2)