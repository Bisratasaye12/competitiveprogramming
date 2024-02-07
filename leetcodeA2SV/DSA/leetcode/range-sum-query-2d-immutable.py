class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.n, self.m = len(self.matrix), len(self.matrix[0])
        self.pre_mat = [[0]*(self.m + 1) for i in range(self.n + 1)]
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                self.pre_mat[i][j] = self.pre_mat[i-1][j] + self.pre_mat[i][j-1] + self.matrix[i - 1][j - 1] - self.pre_mat[i-1][j-1]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = self.pre_mat[row2+1][col2+1] - self.pre_mat[row2+1][col1] - self.pre_mat[row1][col2+1] + self.pre_mat[row1][col1]
        #print(self.pre_mat)
        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)