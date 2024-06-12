'''
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.

Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

Example 1:

Input: intervals = [[1,3],[1,5],[6,7]]
Output: [[1,5],[6,7]]

Example 2:

Input: intervals = [[1,2],[2,3]]
Output: [[1,3]]

'''

# TC: O(n logn)
# SC: O(n) - Worst is that there are no overlaps and all lists within a list has to be appended

def mergeIntervals(intervals):
    if not len(intervals):
        return []

    # Sort the intervals based on the start time
    intervals.sort(key = lambda interval: interval[0])

    # Store the initial list in the output for next interval comparisons
    outputIntervals = [intervals[0]]

    # Start with index 1 Check if the current interval overlaps with the previous one - that's why we added first element to outputIntervals & to handle the edge case.
    for index in range(1, len(intervals)):
        interval = intervals[index]
        current_start = interval[0]
        current_end = interval[1]

        prev_end = outputIntervals[len(outputIntervals) - 1][1] # Returns the last interval that is added or can also be as outputIntervals[-1][1]

        # If there is an overlap between current and previous intervals merge them
        if current_start <= prev_end:
            outputIntervals[-1][1] = max(current_end, prev_end)
        # Add the Interval to the output
        else:
            outputIntervals.append([current_start, current_end])

    return outputIntervals

intervals = [[1, 4], [7, 9], [2, 5]]
print(mergeIntervals(intervals))

intervals = [[1, 2], [2, 3]]
print(mergeIntervals(intervals))

intervals = [[1, 2], [4, 5]]
print(mergeIntervals(intervals))

intervals = []
print(mergeIntervals(intervals))