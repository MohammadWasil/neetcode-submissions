class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        [
            [1,1,1],
            [1,1,0],
            [1,0,1]
        ]
        sr=1, sc=1, color=2
        visited = ((1, 1))

            [1,1,1],
            [1,2,0], # change [1,1] value to 2
            [1,0,1]

            From [1,1], 
            L R, U, and D, if the have same color/value, chaneg them as well.

            [1,2,1],
            [2,2,0], # change [1,1] value to 2
            [1,0,1]
            visited = ((1, 1), (0, 1), (1, 0))

            From [0,1], 
            L R, U, and D, if the have same color/value, chaneg them as well.
            U is OoB, D is already visited, L and R needs to be canges -> visited((0,0), (0,3))
            visited = ((1, 1), (0, 1), (1, 0), (0,0), (0,3))

            [2,2,2], # change [0,0] and (0,3) value to 2
            [2,2,0], 
            [1,0,1]

            from [1, 0]
            U is visited, R is visted, R is OoB, go Down, visited = (2, 0)
            visited = ((1, 1), (0, 1), (1, 0), (0,0), (0,3), (2, 0))
            
            [2,2,2],
            [2,2,0], 
            [2,0,1] # change [2,0] value to 2

            from (0, 0) -> all return False
            from (0, 3) -> D is 0, all return False
            from (2, 0) -> R is 0, all return False
        """

        ROWS = len(image)
        COLS = len(image[0])

        original_color = image[sr][sc]
        image[sr][sc] = color

        #def bfs(r, c, original_color, color):
        visited = set()
        queue = deque()
        queue.append((sr,sc))

        visited.add((sr, sc))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                next_row = r + dr
                next_col = c + dc
                if next_row in range(ROWS) and next_col in range(COLS) and (next_row, next_col) not in visited and image[next_row][next_col] == original_color:

                    image[next_row][next_col] = color
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col))
        #bfs(sr, sc, original_color, color)
        return image