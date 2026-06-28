class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        total_row = len(matrix)
        total_col = len(matrix[0])
        self.prefix_mat = [[0] * (total_col + 1) for _ in range(total_row + 1) ]
        for i in range(total_row):
            for j in range(total_col):
                self.prefix_mat[i][j] = matrix[i][j] + self.prefix_mat[i-1][j] + self.prefix_mat[i][j-1] - self.prefix_mat[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottom_right = self.prefix_mat[row2][col2]
        remove_upper_col2 = self.prefix_mat[row1 - 1][col2]
        remove_left_row1 = self.prefix_mat[row2][col1 - 1]
        add_one_diagonal_value = self.prefix_mat[row1 - 1][col1 - 1]

        return bottom_right - remove_upper_col2 - remove_left_row1 + add_one_diagonal_value


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2) 