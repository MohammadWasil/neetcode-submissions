class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        [
            [1,1,0,0],
            [1,0,0,0],
            [1,1,1,0],
            [0,0,1,1]
        ]
        
        When we get 1st grid on queue, perimeter = 4, (4 sides)
        Then check their neighbouring grid in L,R,U,D, and add them to the queue, if island.
        And at the sam time, remove 1 from permeter (for attached square), and 3 for the three sids for the new grid, 
        i.e., perimeter = perimeter - 1 + 3
        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = []
        
        def bfs(r, c):
            perimeter = 0
            queue = deque()
            queue.append((r, c))
            visit.append((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    if (row+dr) not in range(ROWS) or (col+dc) not in range(COLS) or grid[row+dr][col+dc] == 0:                        
                        perimeter += 1
                    elif (row+dr, col+dc) not in visit:
                        visit.append((row+dr, col+dc))
                        queue.append((row+dr, col+dc))
            
            return perimeter

        for r in range(ROWS):
            for c in range(COLS):
                
                if grid[r][c] == 1 and (r, c) not in visit:
                    perimeter = bfs(r,c)

        return perimeter
