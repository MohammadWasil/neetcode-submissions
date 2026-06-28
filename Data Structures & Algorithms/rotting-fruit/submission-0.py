class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        #visit = set()
        queue = deque()

        fresh = 0
        # sine we need ot start from somewhere, we need to find
        # the position of rotten fruit.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1            
                if grid[r][c] == 2:            
                    #visit.add((r,c)) # find the position where fruit is rotten
                    queue.append((r,c)) # find the position where fruit is rotten
        
        min_time = 0
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for dr, dc in direction:
                    # fnd the next position
                    #if r+dr in range(ROWS) and c+dc in range(COLS) and grid[r+dr][c+dc]==0 and (r+dr,c+dc) in visit:
                    #    continue
                    
                    if r+dr in range(ROWS) and c+dc in range(COLS) and grid[r+dr][c+dc]==1:
                        queue.append((r+dr, c+dc))
                        grid[r+dr][c+dc] = 2
                        fresh -= 1
            min_time += 1
        
        return min_time if fresh == 0 else -1








