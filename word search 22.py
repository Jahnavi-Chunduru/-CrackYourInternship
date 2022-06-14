class Solution:
    def explore(self, i, j, word, visited):
        if tuple([i, j]) in visited:
            return False
        
        if not word:
            return True
        
        found = False
        nxt = word[0]
        
        visited.add(tuple([i, j]))
        if (i + 1) < self.m and nxt == self.board[i + 1][j]:
            found = found or self.explore(i + 1, j, word[1:], visited.copy())
        if (i - 1) >= 0 and nxt == self.board[i - 1][j]:
            found = found or self.explore(i - 1, j, word[1:], visited.copy())
        if (j + 1) < self.n and nxt == self.board[i][j + 1]:
            found = found or self.explore(i, j + 1, word[1:], visited.copy())
        if (j - 1) >= 0 and nxt == self.board[i][j - 1]:
            found = found or self.explore(i, j - 1, word[1:], visited.copy())
        
        return found
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == word[0] and self.explore(i, j, word[1:], set()):
                    return True
        return False
