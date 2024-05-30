# Graph Node: Contains 2 things val or vertex and neighbors list

class GraphNode:
    def __init__(self, val):
        self.val = val # Vertex
        self.neighbors = [] # List containing pointers of others vertexes to which this vertex has an edge or points too

# Instead of using the graph node we can also use HashMap to represent a graph
graphAdjList = { "A": [], "B": ["C", "D"] } # A has no edge to any other vertex; B has an edge towards C and D - Directed Graph

# We can also represent a graph using a Adjancency Matrix - 2D matrix or grid => V X V dimensions => list of lists / array of arrays
'''

            0   1   2   3   4
            A   B   C   D   E   
      [
0 A         0   0   0   0   0    
1 B         1   1   0   0   0
2 C         0   0   0   1   1
3 D         1   0   0   0   1
4 E         1   0   0   0   0
      ]

'''
adjMatrix = [
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 0]
            ]

print(adjMatrix[1][0]) # 1 => means that there is an edge from vertex 1 i.e. B to vertex 0 i.e. A
print(adjMatrix[0][1]) # 0 => means that there is no edge from vertex 0 i.e. A to vertex 1 i.e. B

# Given directed edges, create an adjacency list to represent a graph ["A", "B"] means A -> B

edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
adjList = {} # Create a HashMap to build an adjacency list

for src, dest in edges:
    # Check if the src vertex exists in the hashmap or not
    if src not in adjList:
        adjList[src] = [] # To store neighbors of the vertex
    
    # Also check if the dest vertex exists or not because even if the vertex has no outer edge we still want it with [] empty list to capture all the vertexes
    if dest not in adjList:
        adjList[dest] = []

    # If exists within the src vertex's neighbors i.e. keep adding the dest to represent the edges
    adjList[src].append(dest) # Since in directed edges A -> B i.e. source points to destination

print('Adjacency List => ', adjList)