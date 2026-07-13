class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        [
            [0,1,1,0,1],
            [1,0,1,0,1],
            [0,1,1,0,1],
            [0,1,0,0,1]
        ]
        """
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = []
        max_area = 0
        
        def bfs(r, c):
            area_island = 1
            queue = deque()
            visit.append((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    if (row+dr) in range(ROWS) and (col+dc) in range(COLS) and grid[row+dr][col+dc] == 1 and (row+dr, col+dc) not in visit:
                        visit.append((row+dr, col+dc))
                        queue.append((row+dr, col+dc))
                        area_island += 1
                        
            return area_island

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    island = bfs(r, c)

                    max_area = max(island, max_area)
        
        return max_area