# Problem 1: Implement a function that merges two sorted list of m and n elements respectively, into another sorted list.

# Simple Python Approach - TC: O(n * log(n))

list1 = [1, 1, 2, 5, 8]
list2 = [3, 4, 6]

# Merge 2 lists
list1.extend(list2) # O(n)

# Sort the list
sortedMergedList = sorted(list1)  # O(n * log(n))

print(sortedMergedList)