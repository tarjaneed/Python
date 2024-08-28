'''
Subsets:

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''

# TC: At every index we have 2 choices - Either take or not take, so for n indexes - O(2 power n)
# SC: O(n) - Size of the input - at any given time max recursive calls waiting can be equal to that of the length of the input

'''
Approach:
- At every index we have 2 choices - Either take or not take.
- Start from index 0 and maintain an array that returns us a subsequence or subset everytime current index that we have hits the length of the original input given
    - First we can consider the current index element to be a part of the subsequence, then we call the function again recursively with next index and repeat same thing - to take or not take
    - Second we do not consider the index element to be the part of the subsequence, then we call the function again recursively with next index and repeat same thing - to take or not take.

- For every recursive call first take will be finished till the depth and then for the very last recursive call not take would execute and then it would be returned 
to the previous waiting recursive call.

output = []

func(index, subsequence, nums):

    Base condition:

        if index == len(nums):
            add subsequence to the output
            return

    # Take the element to be considered in the subsequence -> add it to the subsequence array
    subsequence.add(nums[index])
    # Check for the next index considering the above element as a part of the sequence
    func(index + 1, subsequence, nums) - Until this finished for all depth calls the code below it would not execute only after this function finished it start the execution.
    
    # Do not take the element - do not consider the element to be the part of the subsequence and check for the next index without it.
    subsequence.remove(arr[index]) # Or remove the last element
    # Check for the next index not considering the element as a part of the sequence this time
    func(index + 1, subsequence, nums)

func(0, [], nums)
return output
'''

def subsets(index, subseq, nums):
    global output

    if index == len(nums):
        output.append(subseq.copy())
        return

    # Consider the current index element
    subseq.append(nums[index])
    subsets(index + 1, subseq, nums)

    # Do not consider
    subseq.pop()
    subsets(index + 1, subseq, nums)

global output
output = []
nums = [1,2,3]
subsets(0, [], nums)
print(output)

output = []
nums = [0]
subsets(0, [], nums)
print(output)