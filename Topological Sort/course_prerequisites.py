'''
Find the order in which the courses can be taken

0 - ML
1 - Advanced AI
2 - AI
3 - DS

Input: Vertices = 4, Edges = [[3, 2], [3, 0], [2, 0], [2, 1]]
Output: [3, 2, 1, 0] or [3, 2, 0, 1]

Taking Advanced AI is dependent on taking AI [2, 1]
Taking AI is dependent on DS [3, 2]
Taking ML is dependent on DS and AI [3, 0] and [2, 0]

so first we take DS, then AI, then either ML or AI first
i.e. 3, 2, 1, 0 or 3, 2, 0, 1
'''
from collections import deque

def topological_order(vertices, edges):
    # Initialize 2 adjacency lists based on the vertices given one that holds information about the children for each node and other that holds count for the incoming edges on the nodes
    graph = {}
    inDegree = {}

    for i in range(0, vertices):
        graph[i] = [] # Initialize empty list to append the children
        inDegree[i] = 0 # Initial count make it 0

    # Update or Build the graph and inDegree
    for edge in edges:
        parent = edge[0]
        child = edge[1]

        graph[parent].append(child) # Append child to parent's list
        inDegree[child] += 1 # Increment incoming edge for the child. Since there is an edge from parent to child the child has dependency on parent.

    # Now from the inDegree check the vertes that has count 0 to consider them as the source vertices
    sources = deque()

    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    result = []
    # Loop till sources has some value
        # ;then pop the front element from the source add it to the result (Note since it is 0);
        # then for each source check its children; decrement the count; 
        # check if count 0 add it to sources to be considered the next time
    while len(sources):
        vertex = sources.popleft()
        result.append(vertex)

        for child in graph[vertex]: # Check the node's children one by one to; decrement count when you see it and check if they can be added to the sources (when count becomes 0)
            inDegree[child] -= 1

            if inDegree[child] == 0:
                sources.append(child)
    
    return result

vertices = 4
edges = [[3, 2], [3, 0], [2, 0], [2, 1]]

print(topological_order(vertices, edges))