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