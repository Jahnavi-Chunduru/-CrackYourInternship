class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix) + 1
        n = len(matrix[0]) + 1
        self.prefix =  [[0 for i in range(n)] for j in range(m)]
        for i in range(1,m): 
            for j in range (1,n):
                self.prefix[i][j] = self.prefix[i-1][j]+ self.prefix[i][j-1] + matrix[i-1][j-1] - self.prefix[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
