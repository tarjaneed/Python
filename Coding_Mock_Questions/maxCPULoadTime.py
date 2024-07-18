'''
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. 
Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Example 1:
Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7

Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the jobs are running at the same time i.e., during the time interval (2,4).
'''

'''
Approach:

- Sort the jobs based on the start time
- Initialize cpu_load time = jobs[0][2] if atleast 1 job present
- Next start loop from 1 till len(jobs):
    check if the start time of current job < the end of the previous job:
        if yes we found an overlap meaning 2 jobs on same machine
        add this job's cpu time to the cpu_load_time
        cpu_load_time += jobs[j][2]

    in case of no overlap return max of all the jobs
- return cpu_load_time
'''

# TC: O(nlogn) (Since Sorting is done) SC: O(1) - Since sorting is performed in-place

def findMaxCPULoadTime(jobs):

    if len(jobs) == 0:
        return 0

    # Sort based on the start time
    jobs.sort(key = lambda job: job[0])

    cpu_load_time = jobs[0][2]

    for i in range(1, len(jobs)):
        if jobs[i][0] < jobs[i - 1][1]:
            cpu_load_time += jobs[i][2]
        else:
            cpu_load_time = max(cpu_load_time, jobs[i][2])

    return cpu_load_time

jobs = [[1, 4, 3], [7, 9, 6], [2, 5, 4]]
print(findMaxCPULoadTime(jobs))

jobs = [[6, 7, 10], [2, 4, 11], [8, 12, 15]]
print(findMaxCPULoadTime(jobs))