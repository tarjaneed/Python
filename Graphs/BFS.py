from collections import deque

# Perform BFS on a graph which is represented by Adjacency List - TC: O(V)

def BFS(graph, source):
    result = [] # result
    queue = deque() # Keeps track of what is to be visited next
    visited = set() # Keeps the track of the visited nodes

    queue.append(source)
    visited.add(source)
    result.append(source)

    while len(queue):
        vertex = queue.popleft() # node

        # Append node's neighbors to the queue to process at the next level -> in tree BFS we had left and right; only 
        # difference in graph we also keep track of the visted nodes or vertexes

        # For each neighbor of the vertex i.e. each element of the list check whether it is already visited or not; if not add else move ahead
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                result.append(neighbor)
    return result


edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
adjList = {}

for src, dest in edges:
    if src not in adjList:
        adjList[src] = []
    
    if dest not in adjList:
        adjList[dest] = []

    adjList[src].append(dest)

print('Adjacency List => ', adjList)

result = BFS(adjList, "A")

print('BFS on graph => ', result)