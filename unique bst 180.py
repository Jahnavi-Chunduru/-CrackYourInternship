class Solution:
    def numTrees(self, n: int) -> int:                
        return sum(self.numTrees(i) * self.numTrees(n - i - 1) for i in range(n)) if n > 1 else 1
