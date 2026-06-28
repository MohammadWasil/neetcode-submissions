class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        # prefix sum on row only.
        #matrix = self.matrix
        #self.prefix_sum = [[0] * len(self.matrix[0]) for i in range(len(self.matrix))]

        #for r in range(len(self.matrix)):
        #    self.prefix_sum[r][0] = self.matrix[r][0]
        #    for c in range(1, len(self.matrix[0])):
        #        self.prefix_sum[r][c] = self.prefix_sum[r][c-1] + self.matrix[r][c]

        # prefix sum on row and column both.
        COL = len(matrix[0])
        ROW = len(matrix)
        self.prefix_sum = [[0] * (COL + 1) for _ in range(ROW + 1)]

        for r in range(ROW):

            #prefix_sum[r][0] = matrix[r][0]
            for c in range( COL):
                self.prefix_sum[r][c] = matrix[r][c] + self.prefix_sum[r][c-1] + self.prefix_sum[r-1][c] - self.prefix_sum[r-1][c-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # brute force
        #sum_matrix = 0
        #3for r in range(row1, row2+1):
        #    for c in range(col1, col2+1):
        #        sum_matrix += self.matrix[r][c]
        #return sum_matrix

        # how to do it with O(1) time complexity.
        # self.prefix_sum <
        #sum_matrix = 0
        #for r in range(row1, row2+1):
        #   if col1 > 0:
        #        sum_matrix += (self.prefix_sum[r][col2] - self.prefix_sum[r][col1 - 1])
        #    else:
        #        sum_matrix += self.prefix_sum[r][col2]
        #return sum_matrix

        #row1, col1, row2, col2 = [2, 1, 4, 3]
        #row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        sum_matrix = 0
        total_area = self.prefix_sum[row2][col2]
        remove_top_area = self.prefix_sum[row1 - 1][col2]
        remove_left_area = self.prefix_sum[row2][col1 - 1]
        retain_top_left_block = self.prefix_sum[row1 - 1][col1 - 1]
        
        sum_matrix = total_area - remove_top_area - remove_left_area + retain_top_left_block
        return sum_matrix




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)