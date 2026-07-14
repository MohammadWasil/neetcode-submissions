class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        [
            [1,1,0],
            [0,1,1],
            [0,1,2]
        ]
        start with (2,2) -> add to visit (2, 2), and queue
        minute = 0
        find their neighbours 
            remove from the queue (2,2)
            (2, 2) -> (1,2) and (2,1), rest is OoB
            check if val == 1 and not OoB
                yes -> change them 2, add to visited, and queue
                minute += 1
        """

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        
        minute = 0
        fresh = 0
        
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2: # and (r, c) not in visited:
                    queue.append((r, c))
                    visited.add((r, c))        
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for dr, dc in directions:
                    next_row = r + dr
                    next_col = c + dc

                    if next_row in range(ROWS) and next_col in range(COLS) and grid[next_row][next_col] == 1:
                        grid[next_row][next_col] = 2
                        queue.append((next_row, next_col))
                        visited.add((next_row, next_col))
                        fresh -= 1
        
            minute += 1
        return minute if fresh == 0 else -1


