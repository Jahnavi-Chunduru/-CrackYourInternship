class Solution(object):
    def maximalSquare(self, matrix):
        def val(i,j):
            if(0<=i<len(matrix) and 0<=j<len(matrix[0])):
                return int(matrix[i][j])
            else:
                return 0
        maxSize = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(val(i,j) == 1):
                    matrix[i][j] = min(val(i-1,j-1),val(i-1,j),val(i,j-1))+1
                    maxSize = max(maxSize,matrix[i][j])
        return maxSize*maxSize
