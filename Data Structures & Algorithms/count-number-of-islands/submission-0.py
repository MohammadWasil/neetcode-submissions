class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        - grid can be empty
        - always contains 0s and 1s
        - only one elemtn cannot be an island
        [
            ["1","1","0","0","1"],
            ["1","1","0","0","1"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        visit => [[0,0], ] -> no removal
        
        if [0, 0] is a 1 or not, and they are not visited before
        BFS:
        queue => # tells us to run BFS on these points as well.
                 # once processed, we can just remove the value
            
            [0,0] ---neighbors--> [0,1], [1, 0] -> 
                - if the new neighbour is valid (for both r and c)
                - if they have 1 -> 
                - if they are not visited before
                ====> add to visit
                ====> add to queue
            remove [0,0] from the queue
            visit => [[0,0], [0,1], [1, 0]]
            queue => [[0,1], [1, 0]]
            Continue with the BFS([0, 1])
            visit => [[0,0], [0,1], [1, 0], [1, 1]]
            queue => [[1, 0], [1, 1]]

            Continue with the BFS([1, 0])
            visit => [[0,0], [0,1], [1, 0], [1, 1]]
            queue => [[1, 1]]

            Continue with the BFS([1, 1])
            visit => [[0,0], [0,1], [1, 0], [1, 1]]
            queue => []
            once the queue is complete -> BFS ==> Island += 1

            BFS([0, 5])
            visit => [[0,0], [0,1], [1, 0], [1, 1], [0, 5]]
            queue => [[0, 5], ]

        downward
        visit => [[0,0], [0,1], [1, 0], [1, 1], [0, 5], [1, 5]]
        queue => [[1, 5], ]

        BFS([1, 5])
            visit => [[0,0], [0,1], [1, 0], [1, 1], [0, 5], [1, 5]]
            queue => []
            once the queue is complete -> BFS ==> Island += 1
        """

        # grid can be empty
        if not grid:
            return 0

        visit = set()       # hold all the 1's we ever visited
        
        island = 0          # counter

        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c):
            queue = deque()     # hold all the 1's where we need to run our BFS on
            visit.add((r, c))
            queue.append([r, c])

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # D, U, R, L

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    if row+dr in range(ROWS) and col+dc in range(COLS) and grid[row+dr][col+dc] == "1" and (row+dr, col+dc) not in visit:

                        visit.add((row+dr, col+dc))
                        queue.append([row+dr, col+dc])


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    # run bfs on the point
                    bfs(r, c)
                    island += 1
        
        return island

        


        