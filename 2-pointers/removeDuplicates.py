'''
Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element appears only once. 
The relative order of the elements should be kept the same and you should not use any extra space so that that the solution have a space complexity of 0(1).
    Move all the unique elements at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.
• Example 1:
    • Input: [2, 3, 3, 3, 6, 9, 9]
    • Output: 4
    • Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
'''

# TC: O(n) and SC: O(1) since in-place

def removeDuplicates(arr):
    if len(arr) == 1:
        return 1

    left = 0 # Keeps track of the unique element and by default 1st element i.e. on 0th index is unique
    right = 1 # Moves ahead till it finds the unique element to send it to left to be replaced

    while right < len(arr):
        if arr[left] != arr[right]:
            left += 1
            arr[left] = arr[right]
        right += 1

    print('Sub Array:', arr[0:left + 1])

    return (left + 1)

nums = [2]
print('Single element:', removeDuplicates(nums))

nums = [2, 2]
print('Unique Element Count:', removeDuplicates(nums))

nums = [2, 3]
print('Unique Element Count:', removeDuplicates(nums))

nums = [2, 3, 3, 3, 6, 9, 9]
print('Unique Element Count:', removeDuplicates(nums))