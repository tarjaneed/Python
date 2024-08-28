# Reverse an array

# TC: O(n) - approx. n/2 function calls
# SC: O(n)

def array_reverse(arr, l, r):

    if l >= r: # This means mid is reached and swaps are done. No more swaps are to be done.
        return

    # else swap

    [arr[l], arr[r]] = [arr[r], arr[l]]

    return array_reverse(arr, l + 1, r - 1)

arr = [1, 2, 3, 5]
array_reverse(arr, 0, len(arr) - 1)
print(arr)