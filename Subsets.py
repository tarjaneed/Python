'''
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

'''

'''
Approach:
- We start by adding empty list to the output array => output = [[]]
- Then we loop through the nums/input array and every time we got to an element:
    - we copy the previous output that we had + add this new number to each of the list that we have seen so far.
    - This keeps on doubling the list too
[1, 2, 3]
        []      =>  1
  1:  [],[1]    =>  2
  2:  [], [1], [2], [1, 2]  => 4
  3:  [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]  => 8

2 power n

TC: O(n * 2 power n)
SC: O(2 power n)
'''

def findSubsets(nums):
    output = [[]] # Start by saving empty subset to the output.

    for num in nums:
        # Shorthand: Copy the previous output to output and for each list in previous output add this number (concat) we are traversing
        # output += [lst + [num] for lst in output]

        # Add this number to all the subsets we have seen so far i.e. in the lists that output holds
        new_subsets = []
        for lst in output:
           new_subsets.append(lst + [num])

        output += new_subsets # Copy previous output + add new subsets
    return output

nums = [1, 2, 3]
print(findSubsets(nums))

nums = [0]
print(findSubsets(nums))