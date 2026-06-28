class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Always 0s and 1s
        no island -> return 0
        empty grid -> return 0

        [0,1,1,0,1],
        [1,0,1,0,1],
        [0,1,1,0,1],
        [0,1,0,0,1]

        visited = []
        max_area_island = 0

        chck if value is 1
        if it has already been visited before
        [0, 0] -> No
        [0, 1] -> Yes -> we can bfs on this cell
                <- area_island vs maax_area_island

        BFS -> [0, 1]
            visited = [[0, 1]]
            queue = [[0, 1]]

            loop thorugh the queue
            pop the queue
                get all the neigbours of the current cell
                and check if they are 1, check the bounds, and check f they have been visited bfore
                    then visit the nieghbours by adding them to the visited
                    visited = [[0, 1], [0, 2]]
                    add tot he queue to bfs on [0, 2] as well.
                    area_island += 1

            return area_island

        """
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()
        max_area_island = 0 

        def bfs(r, c):
            queue = deque()
            visit.add((r, c))
            queue.append([r, c])
            area_island = 1 # counting the starting cell, the one where (r,c) is already 1

            # to find the neighbours
            directions = [[1,0], [-1,0], [0, 1], [0, -1]]

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    if row+dr in range(ROWS) and col+dc in range(COLS) and grid[row+dr][col+dc] == 1 and (row+dr, col+dc) not in visit:

                        visit.add((row+dr, col+dc))
                        queue.append([row+dr, col+dc])
                        area_island += 1
            return area_island

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area_island = bfs(r, c)
                    if area_island > max_area_island:
                        max_area_island = area_island
                    
        
        return max_area_island
