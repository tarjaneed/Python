'''
There are ’N’ tasks, labeled from ‘0’ to ’N - 1’. Each task can have some prerequisite tasks which need to be completed before it scheduled. 
Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

Input: Tasks = 6, Prerequisites = [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]
Output: true

Input: Tasks = 3, Prerequisites = [[0, 1], [1, 2], [2, 0]]
Output: false
'''

from collections import deque

def taskScheduling(vertices, edges):
    graph = {}
    inDegree = {}

    # Initialize adjacency lists
    for i in range(0, vertices):
        graph[i] = []
        inDegree[i] = 0

    # Build the graph and inDegree lists
    for edge in edges:
        parent = edge[0]
        child = edge[1]

        graph[parent].append(child)
        inDegree[child] += 1

    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    sorted_order = []

    while len(sources):
        vertex = sources.popleft()
        sorted_order.append(vertex)

        # Iterate through each child of the vertex
        for child in graph[vertex]:
            inDegree[child] -= 1

            if inDegree[child] == 0:
                sources.append(child)

    # All tasks can only be scheduled if graph has no cycle i.e. it should be a DAG to apply topological sort
    # Graph has a cycle if length of the sorted order we found does not match number of vertices given
    return vertices == len(sorted_order) 

tasks = 6
prerequisites = [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]
# Valid Sorted Order = [0, 1, 3, 4, 2, 5] or [0, 1, 4, 3, 2, 5] or [1, 0, 3, 4, 2, 5] or [1, 0, 4, 3, 2, 5]
print(taskScheduling(tasks, prerequisites))

tasks = 3
prerequisites = [[0, 1], [1, 2], [2, 0]]
print(taskScheduling(tasks, prerequisites))