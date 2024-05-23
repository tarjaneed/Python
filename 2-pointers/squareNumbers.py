'''
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.
Example 1:
    Input: [-2, -1, 0, 2, 3]
    Output: [0, 1, 4, 4, 9]
'''

'''
TC: O(n) - since we are traversing the list, squaring the element at indexes; comparing them; storing them
SC: O(n) - we are creating a new result array of size of input array/list
'''

def squareNumbers(arr):
    n = len(arr)
    squared_arr = [None] * n # Create a new array of size n

    left = 0
    right = n - 1
    k = n - 1

    while left <= right:
        squared_left = arr[left] * arr[left]
        squared_right = arr[right] * arr[right]

        if squared_left > squared_right:
            squared_arr[k] = squared_left # Update element with the squared one at that index since we already defined an array
            left += 1
        else:
            squared_arr[k] = squared_right 
            right -= 1
        k -= 1

    return squared_arr

nums = [-2, -1, 0, 2, 3]
print(squareNumbers(nums))

nums = [0, 1, 2, 3]
print(squareNumbers(nums))