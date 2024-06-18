'''
Problem 1: Given an array of intervals representing ’N’ appointments, find out if a person can attend all the appointments.

Appointments: [[1, 4], [2,5], [7, 9]]
Output: false

Explanation: Since [1, 4] and [2, 5] overlap, a person cannot attend both of these appointments.


Similar Problem 2:

Given a list of appointments, find all the conflicting appointments.

Example:

Appointments: [[4, 5], [2, 3], [3, 6], [5, 7], [7, 8]]
Output:

[4, 5] and [3, 6] conflict.
[3, 6] and [5, 7] conflict.
'''

'''
Approach:

Problem 1:

Check if there is any overalapping apppointment, if there is it means a person cannot attend all the appointments.
Assuming that if there are no appointments a person cannot attend them hence returning False.

Problem 2:

Check if there are any overalapping apppointments, if there are append them to conflict list.
'''

# Problem 2: TC: O(n logn) - Since sorting is performed SC: O(n) - Worst case all could be conflicting
# For this we also have to do merge intervals. since we need to check all conflicts and return them
def findConflictingAppointements(appointments):
    if len(appointments) == 0:
        return False

    # Sort the appointments based on the start time
    appointments.sort(key = lambda appointment: appointment[0])

    outputIntervals = [appointments[0]]
    conflicting_appointments = []
    # Check for an overlap; as soon as you find the first overlap, return False else return True
    # Overlaps if the start time of the appointment we are checking is smaller than the end time of the appointment we saw before it
    for index in range(1, len(appointments)):
        appointment = appointments[index]
        current_start = appointment[0]
        current_end = appointment[1]

        prev_start = outputIntervals[len(outputIntervals) - 1][0]
        prev_end = outputIntervals[len(outputIntervals) - 1][1] # Returns the last interval that is added or can also be as outputIntervals[-1][1]

        # If there is an overlap between current and previous intervals merge them
        if current_start < prev_end:
            conflicting_appointments.append([[prev_start, prev_end], appointment])
            outputIntervals[-1][1] = max(current_end, prev_end)
        # Add the Interval to the output
        else:
            outputIntervals.append([current_start, current_end])

    return conflicting_appointments

# Problem 1: TC: O(n logn) - Since sorting is performed SC: O(1)
def findOverlap(appointments):
    if len(appointments) == 0:
        return False

    # Sort the appointments based on the start time
    appointments.sort(key = lambda appointment: appointment[0])

    # Check for an overlap; as soon as you find the first overlap, return False else return True
    # Overlaps if the start time of the appointment we are checking is smaller than the end time of the appointment we saw before it
    i = 0
    for j in range(1, len(appointments)):
        if appointments[j][0] < appointments[i][1]: # Overlap Found
            return False
        i += 1

    return True

appointments = [[1, 4], [7, 9], [2, 5]]
print(findOverlap(appointments))
print(findConflictingAppointements(appointments))

appointments = [[1, 4], [5, 6], [7, 9]]
print(findOverlap(appointments))
print(findConflictingAppointements(appointments))

appointments = [[1, 3], [5, 6], [7, 9], [4, 8]]
print(findOverlap(appointments))
print(findConflictingAppointements(appointments))

appointments = [[4, 5], [2, 3], [3, 6], [5, 7], [7, 8]]
print(findOverlap(appointments))
print(findConflictingAppointements(appointments))
