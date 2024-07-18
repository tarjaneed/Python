'''
Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.
Example 1:
Meetings: [[1,4], [2,5], [7,9]]
Output: 2

Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can occur in any of the two rooms later.
'''

'''
Approach:

- Check that atleast 1 meeting exists if not simply return 0 i.e. 0 rooms would be needed
    if len(meetings) == 0:
        return 0
- If meetings present:
    Initialize no_of_rooms = 1 (since we know atleast one meeting would be there)
- Now, sort the meetings as per the start_time - ascending order
- Loop from 1 to len(meetings):
    check if the start_time of the meeting we are currently checking i.e. meetings[i][0] is < that the previous meeting's end_time i.e. meetings[i - 1][1]
    if it is < that means we found an overlap hence we would need one extra room to conduct both these meetings => no_of_rooms += 1
- At the end of loop return no_of_rooms
'''

import heapq

# TC: O(nlogn) => O(nlogn) SC: O(n) can have all meetings overlap

def no_of_rooms(meetings):
    if len(meetings) == 0:
        return 0
    
    meetings.sort(key = lambda meeting: meeting[0]) # Sort by the start time # [[1,4], [2,5], [7,9]]
    no_of_rooms = [] # Holds number of rooms needed

    heapq.heappush(no_of_rooms, meetings[0][1]) # Push 1st meeting's end time to the min heap

    for i in range(1, len(meetings)): # 1 - 2 1 2 
        # Overlaps - if 2nd meetings's start time is < previous meeting's end time (from heap top element)
        if meetings[i][0] < no_of_rooms[0]:
            # We need more rooms to conduct all meetings - push end time of the current meeting in the min-heap
            heapq.heappush(no_of_rooms, meetings[i][1])
        else:
            # If no overlap pop from the min-heap since the top would be free and reuse it for the new meeting hence we push end-time of this meeting
            heapq.heappop(no_of_rooms)
            heapq.heappush(no_of_rooms, meetings[i][1])

    return len(no_of_rooms) # 2

meetings = [[1, 4], [2, 5], [7, 9]]
print(no_of_rooms(meetings))

meetings = [[6, 7], [2, 4], [8, 12]]
print(no_of_rooms(meetings))

meetings = [[1, 4], [2, 3], [3, 6]]
print(no_of_rooms(meetings))

meetings = [[4, 5], [2, 3], [2, 4], [3, 5]]
print(no_of_rooms(meetings))