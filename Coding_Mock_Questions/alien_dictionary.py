'''
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.
You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.
If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
'''

from collections import deque

'''
Approach:

Here we need to first create edges edges = [['t', 'f'],['w', 'e']] => t comes before f and so on
Since here vertices are not given and also characters are there and not numbers we need to find the unique set of characters as well from the words given and then use them as vertices to 
build the graph and inDegree indices.
Match pair of words given and break as soon as you find the unmatched character and add it as an edge
Next is we pass edges and unique_characters_list as vertices to the topological sort:
    - It first build the graph and inDegree adjacency lists
    - Then performs BFS to find the order
'''

'''
 Order not possible when:
    1. larger string comes before the smaller one
        Eg: ABCD - S1
            ABC - S2
    2. There is a cycle in the graph
        To check this match the len(sorted) with len(vertices) if they do not match then there is cycle and that the order is not possible
'''

# TC: O(n)

def topologicalSort(edges, vertices):

    result = []

    graph = {} # Hold the info about children for each node
    inDegree = {} # Holds the dependency that each node has

    for vertex in vertices:
        graph[vertex] = []
        inDegree[vertex] = 0

    for edge in edges:
        parent = edge[0]
        child = edge[1]

        graph[parent].append(child)
        inDegree[child] += 1 

    result = []
    sources = deque()

    for vertex in inDegree:
        if inDegree[vertex] == 0:
            sources.append(vertex)

    while len(sources) > 0:
        vertex = sources.popleft()
        result.append(vertex)

        for child in graph[vertex]:
            inDegree[child] -= 1

            if inDegree[child] == 0:
                sources.append(child)

    return result

words = ["wrt", "wrf", "er", "ett", "rftt"]

edges = []

unique_chars = set()

for word in words:
    for char in word:
        unique_chars.add(char)

unique_chars_list = list(unique_chars)

# we go from 0 to 3 since we need to check pairs
for i in range(0, len(words) - 1):
    S1 = words[i]
    S2 = words[i + 1]
    min_len = min(len(S1), len(S2)) # Only check characters till the min length

    # Construct Edges
    for ptr in range(0, min_len):
        if S1[ptr] != S2[ptr]:
            edges.append([S1[ptr], S2[ptr]])
            break

result = topologicalSort(edges, unique_chars_list)

print("".join(result))