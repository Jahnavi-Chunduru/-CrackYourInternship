class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self._uniquePaths(m, n, 0, 0)    
    def _uniquePaths(self, m, n, x, y):   
        if x == m - 1 or y == n - 1:
            return 1
        
        return self._uniquePaths(m, n, x + 1, y) + self._uniquePaths(m, n, x, y + 1)
