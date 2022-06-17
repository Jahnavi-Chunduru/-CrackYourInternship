class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        def expand(row, col, size):
            nonlocal m, n
            frontierRow = row+size-1
            frontierCol = col+size-1
            if frontierRow >= m or frontierCol >= n:
                return False
            for j in range(col, frontierCol+1):
                if not matrix[frontierRow][j]:
                    return False
            for i in range(row, frontierRow+1):
                if not matrix[i][frontierCol]:
                    return False
                
            return True
        
        if len(matrix) == len(matrix[0]):
            maxSize = len(matrix) -1
        else:
            maxSize = min(len(matrix), len(matrix[0]))
        
        for row in range(m):
            for col in range(n):
                for size in range(1, maxSize+1):
                    if expand(row, col, size):
                        count += 1
                    else:
                        break
        return count
