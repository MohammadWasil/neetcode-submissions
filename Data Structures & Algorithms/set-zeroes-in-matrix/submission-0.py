class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROW = len(matrix)
        COL = len(matrix[0])
        zero_row = [False] * ROW
        zero_col = [False] * COL

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    zero_row[r] = True
                    zero_col[c] = True
        
        for r in range(ROW):
            for c in range(COL):
                if zero_row[r] or zero_col[c]:
                    matrix[r][c] = 0


        
        