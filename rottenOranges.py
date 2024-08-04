'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''

from collections import deque

def orangesRotting(grid):
        time = -1

        row_max = len(grid)
        col_max = len(grid[0])

        dq = deque() # []

        '''
        for i in range(0, row_max):
            for j in range(0, col_max):
                print(grid[i][j], end=" ")
            print('\n') 
        '''

        for i in range(0, row_max):
            for j in range(0, col_max):
                if grid[i][j] == 2:
                    dq.append([i, j])
    
        while dq:
            size = len(dq)

            time += 1
            while size:
                element = dq.popleft()

                i = element[0]
                j = element[1]

                grid[i][j] = 2
                #print("CurrentNode ",str(i)," : ", str(j))

                if i - 1 > 0 and grid[i - 1][j] == 1:
                    dq.append([i - 1, j])

                if i + 1 < row_max and grid[i + 1][j] == 1:
                    dq.append([i + 1, j])
                
                if j - 1 > 0 and grid[i][j - 1] == 1:
                    dq.append([i, j - 1])

                if j + 1 < col_max and grid[i][j + 1] == 1:
                    #print(str(i),": ", str(j))
                    dq.append([i, j + 1])

                size -= 1
        
        # for i in range(0, row_max):
        #     for j in range(0, col_max):
        #         print(grid[i][j], end=" ")
        #     print('\n') 

        for i in range(0, row_max):
            for j in range(0, col_max):
                if grid[i][j] == 1:
                    return -1

        return 0 if time == -1 else time

grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(orangesRotting(grid))

grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(orangesRotting(grid))