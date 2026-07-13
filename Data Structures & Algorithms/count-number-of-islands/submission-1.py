class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        [
            ["0","1","1","1","0"],
            ["0","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = []
        island = 0

        def bfs(r, c):
            queue = deque()
            visit.append((r, c))

            queue.append((r, c))

            while queue:
                r, c = queue.popleft()
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

                for dr, dc in directions:
                    if (r + dr) in range(ROWS) and (c + dc) in range(COLS) and grid[r + dr][c + dc] == "1" and  (r + dr, c + dc) not in visit:
                        visit.append((r + dr, c + dc))
                        queue.append((r + dr, c + dc))

        for r in range(ROWS):
            for c in range(COLS):
                # if it is an island,
                # (r,c) not in visit.
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    island += 1
                    
        return island