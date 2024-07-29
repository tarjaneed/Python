'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

'''
Approach:
- Keep incrementing the islands_count in the outer loop of picking the 1's to traverse.
- Start by picking dimensions marked as 1 one at a time i.e. pick land and then perform dfs on it:
    - We need to check the boundary conditions as well i.e. out of bounds conditions for rows and columns of the grid.
    - Continue till you don't find a 0 i.e. water in left, right, top and bottom of that dimension. Return from dfs as soon as you find 0 - This will be true for all the directions else again return
    - Also keep marking the visited land i.e. 1 as 0 to show it as marked so we do not consider it again as a part of the other island.
- return islands_count 
'''

# TC: O(m * n)
# SC: O(m * n) worst case grid is filled with land

def dfs_check_land(grid, r, c, row_max, col_max):

    if r == row_max or c == col_max or r < 0 or c < 0 or grid[r][c] == '0':
        return

    # Mark the current land (1) dimensions as 0 since visited
    grid[r][c] = '0'

    # Find the 1's to find connected islands in different directions
    dfs_check_land(grid, r + 1, c, row_max, col_max) # Bottom
    dfs_check_land(grid, r - 1, c, row_max, col_max) # Up
    dfs_check_land(grid, r, c + 1, row_max, col_max) # Right
    dfs_check_land(grid, r, c - 1, row_max, col_max) # Left

def find_no_of_islands(grid):
    if len(grid) == 0:
        return 0
    
    count_islands = 0

    row_max = len(grid)
    col_max = len(grid[0])

    # O(m * n)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == '1':
                count_islands += 1
                dfs_check_land(grid, i, j, row_max, col_max)

    return count_islands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(find_no_of_islands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(find_no_of_islands(grid))