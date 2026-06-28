class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        [
            [0,1,0]
            [1,0,0]
            [1,1,0]
        ]
        path = 0
        bfs(0, 0)
        # check for 8 directions, and make sure the dirctions are in bound
        # check if the node has been visted vefore, check the node value is only 0
        1. queue = [(0,0), ]
            True: path+=1
                    queue[(1,1)]
                if (r+dr,c+dc) == (n-1, n-1)
                    return path
        """
        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] or grid[ROWS - 1][COLS - 1]:
            return -1
        
        queue = deque()
        queue.append([0,0,1]) # top left corner
        
        visit = set()
        visit.add((0,0))
    
        directions = [[1,0], [-1,0], [0,1], [0, -1],
                      [1,1], [-1,-1], [1, -1], [-1, 1]
                        ]

        while queue:
            row, col, path = queue.popleft()
            if row == ROWS-1 and col == COLS-1:
                return path
            
            for dr, dc in directions:
                new_row = row+dr
                new_col = col+dc
                if new_row in range(ROWS) and new_col in range(COLS) and grid[new_row][new_col] == 0 and (new_row, new_col) not in visit:
                    queue.append([new_row, new_col, path+1])
                    visit.add((new_row, new_col))
                    
        return -1
        